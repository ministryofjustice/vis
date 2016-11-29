#!/bin/bash
cd /app
case ${DOCKER_STATE} in
create)
    echo "Running create"
    python manage.py migrate vis zero
    python manage.py migrate
    python manage.py createsuperuser --username=admin
    python manage.py loaddata glossary helplines police test_pages vis/fixtures/test_users.json
    python manage.py loaddata vis/fixtures/test_users glossary helplines police test_pages
    ;;
migrate)
    echo "Running migrate"
    python manage.py migrate
    ;;
esac

python manage.py fixpccpermissions
python manage.py runserver 0.0.0.0:8000
