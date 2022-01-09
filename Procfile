web: cd /app/backend && gunicorn config.wsgi
release: python manage.py migrate
release: python manage.py collectstatic --noinput