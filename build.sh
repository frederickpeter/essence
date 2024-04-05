#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

#create superuser - only run this once
python manage.py createsuperuser2 --email admin@gmail.com --password 1_Itzpeter --first_name admin --last_name admin --no-input