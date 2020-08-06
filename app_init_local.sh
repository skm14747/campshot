#!/bin/sh
set -e

# echo "Migrating"
# # python manage.py makemigrations
# python manage.py migrate

# Aggregate all static files
echo "Collect static"
# python manage.py collectstatic --noinput

# Start the development server
echo "Runserver"
python manage.py runserver 0.0.0.0:8000
echo "Server started"
