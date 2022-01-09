web: cd /app/frontend && npm run build && npm run start
server: cd /app/backend && gunicorn config.wsgi -b 0.0.0.0:1337
release: python manage.py migrate
release: python manage.py collectstatic --noinput
