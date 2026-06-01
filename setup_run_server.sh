#!/bin/bash
set -e

echo "Starting Prime Trade AI local setup..."

if ! command -v python3 &> /dev/null; then
    echo "Python3 could not be found. Please install Python3 to continue."
    exit 1
fi

if [ ! -d "env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
else
    echo "Virtual environment already exists."
fi

echo "Activating virtual environment..."
source env/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Navigating to the Django project directory..."
cd primetrade_ai

echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Configuring default Superuser account..."
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="admin1234"
export DJANGO_SUPERUSER_EMAIL="admin@primetrade.ai"
python manage.py createsuperuser --no-input || echo "Superuser already exists."

echo "Setup complete! Starting the Django development server..."
echo "You can access the dashboard at: http://localhost:8000/home/"
echo "---------------------------------------------------------"
python manage.py runserver
