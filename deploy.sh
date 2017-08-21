#!/usr/bin/env bash
set -ex

if [ $# -ne 1 ]; then
  >&2 echo "Usage: ./deploy.sh environment"
  exit 1
fi

ENVIRONMENT=$1
GIT_SHA=$(git rev-parse HEAD)
BRANCH_NAME="${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
HEROKU_PATH="${HEROKU_PATH:-$(which heroku)}"

# Check we're deploying the right branch to the right environment
if [ "$ENVIRONMENT" = "staging" ]; then
  if [ "$BRANCH_NAME" != "rob-develop-test" ]; then
    >&2 echo "Can only deploy 'rob-develop-test' to staging, you are on '${BRANCH_NAME}'"
    exit 1
  fi
elif [ "$ENVIRONMENT" = "prod" ]; then
  if [ "$BRANCH_NAME" != "master" ]; then
    >&2 echo "Can only deploy 'master' to prod, you are on '${BRANCH_NAME}'"
    exit 1
  fi
else
  >&2 echo "Unknown environment '${ENVIRONMENT}'. Can be prod or staging."
  exit 1
fi

# Check we have heroku remotes set up correctly
if ! git remote | grep "^heroku-$ENVIRONMENT$" > /dev/null; then
  >&2 echo "Heroku remote not found; expecting heroku-${ENVIRONMENT}"
  exit 1
fi

docker build -t moj-vis .
CONTAINER_ID=$(docker run -d moj-vis)

rm -rf ./static ./vis/assets
mkdir -p ./static ./vis/assets

docker cp $CONTAINER_ID:/app/static ./static
docker cp $CONTAINER_ID:/app/vis/assets ./vis/assets

exit 2

git add -f ./static ./vis/assets
git commit -m 'deploy: add static assets'

git push heroku-${ENVIRONMENT} HEAD:master -f
$HEROKU_PATH config:add GIT_SHA=$GIT_SHA --app vis-${ENVIRONMENT}
$HEROKU_PATH config:add DEPLOY_DATETIME=`date -u +"%Y-%m-%dT%H:%M:%SZ"` --app vis-${ENVIRONMENT}
git reset --hard HEAD^

function current_version {
  url="https://vis-$1.herokuapp.com/ping.json"

  curl -k $url | sed 's/.*commit_id": "\([^"]*\)".*/\1/g'
}

while [ "$(current_version $ENVIRONMENT)" != "$GIT_SHA" ]; do
  sleep 2
done

curl -kq https://vis-staging.herokuapp.com
