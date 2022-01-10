web: gunicorn config.wsgi
release: python manage.py migrate
swagger: python manage.py spectacular --file staticfiles/schema.yml
