### 👉 Installation in a Linux Environment

> Set up the project in a `venv` virtual environment.

#### Project Overview

This project is an API for a simple post management system, built with Django, Django REST Framework, and Vue.js.



1. **Download the repository and set up the environment**   

   ```bash
   # Download the repository

   https://github.com/israelwerther/socialmedia
   

   # Create and activate the virtual environment
   virtualenv venv
   source venv/bin/activate

   # Install dependencies
   pip3 install -r requirements.txt

   # Apply database migrations
   python manage.py migrate


   With a postgres database created, point your .env file to an existing database
   For example: DATABASE_URL=postgres://postgres:postgres@localhost:5432/socialmediadb
   

1. **Access the documentation**   

   ```bash
   Swagger: http://localhost:8000/api/swagger/
   Index project: http://localhost:8000/
   