#!/bin/sh

# Wait for Postgres to start
while ! nc -z db 5432; do
  sleep 0.1
done

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn Learning_Platform.wsgi:application \
  --bind 0.0.0.0:8000 \
#  --workers 4
