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
if [ "$ENVIRONMENT" = "prod" ]; then
  if [ "$BRANCH_NAME" != "master" ]; then
    >&2 echo "Can only deploy 'master' to prod, you are on '${BRANCH_NAME}'"
    exit 1
  fi
elif [ "$ENVIRONMENT" != "staging" ]; then
  >&2 echo "Unknown environment '${ENVIRONMENT}'. Can be prod or staging."
  exit 1
fi

# Check we have heroku remotes set up correctly
if ! git remote | grep "^heroku-$ENVIRONMENT$" > /dev/null; then
  >&2 echo "Heroku remote not found; expecting heroku-${ENVIRONMENT}"
  exit 1
fi

echo ">>> Building static assets"
docker build -t moj-vis .
CONTAINER_ID=$(docker run -d moj-vis)

# Different versions of docker cp treat directories differently
# This approach works for old and new versions
TMP_CP_DIR=$(mktemp -d /tmp/heroku-vis-static.XXXXXXX)
trap "{ rm -rf $TMP_CP_DIR; }" EXIT

rm -rf ./static ./vis/assets
mkdir -p $TMP_CP_DIR/static $TMP_CP_DIR/assets

docker cp $CONTAINER_ID:/app/static/ $TMP_CP_DIR/static
docker cp $CONTAINER_ID:/app/vis/assets/ $TMP_CP_DIR/assets

mv $TMP_CP_DIR/static/static ./static
mv $TMP_CP_DIR/assets/assets ./vis/assets

git add -f ./static ./vis/assets
git commit -m 'deploy: add static assets'

git push heroku-${ENVIRONMENT} HEAD:master -f
$HEROKU_PATH config:add GIT_SHA=$GIT_SHA --app vis-${ENVIRONMENT}
$HEROKU_PATH config:add DEPLOY_DATETIME=`date -u +"%Y-%m-%dT%H:%M:%SZ"` --app vis-${ENVIRONMENT}
git reset --hard HEAD^

function get_url {
  echo "https://vis-$1.herokuapp.com"
}

function current_version {
  curl -k $(get_url $1)/ping.json | sed 's/.*commit_id": "\([^"]*\)".*/\1/g'
}

while [ "$(current_version $ENVIRONMENT)" != "$GIT_SHA" ]; do
  sleep 2
done

curl -Lfsk $(get_url $ENVIRONMENT) > /dev/null || {
  >&2 echo "Failed loading $(get_url $ENVIRONMENT)"
  exit 2
}
