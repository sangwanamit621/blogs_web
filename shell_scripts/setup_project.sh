#!/bin/bash

# Create a new Python environment named blogs_env
echo "Creating new Python environment named blogs_env..."
python3 -m venv blogs_env

# Activate the environment
echo "Activating Python environment..."
source blogs_env/bin/activate

# Install requirements
echo "Installing requirements..."
pip3 install -r requirements.txt

# Make migrations
echo "Running makemigrations..."
python3 manage.py makemigrations

# Migrate
echo "Running migrate..."
python3 manage.py migrate

echo "Tasks completed."
