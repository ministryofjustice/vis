release: python manage.py migrate --noinput
web: waitress-serve --port=$PORT vis.wsgi:application
