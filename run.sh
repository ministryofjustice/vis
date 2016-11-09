#!/bin/bash
cd /app
case ${DOCKER_STATE} in
create)
    echo "Running create"
    ./manage migrate vis zero
    ./manage migrate
    ./manage.py createsuperuser --username=admin
    ./manage.py loaddata glossary helplines police test_pages vis/fixtures/test_users.json
    ;;
migrate)
    echo "Running migrate"
    ./manage migrate
    ;;
esac
uwsgi -c /etc/uwcgi/vis.ini
