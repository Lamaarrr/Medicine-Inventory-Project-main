# Setup Guide

## Install Dependencies
1. Install Python 3.10+.
2. Install MySQL Server.
3. Install Python packages:
   - pip install -r src/requirements.txt

## Configure MySQL
1. Create a database user.
2. Update src/database.py with your credentials.

## Run SQL Scripts
1. Run sql/create_tables.sql
2. Run sql/triggers.sql
3. Run sql/views.sql
4. Run sql/load_data.sql

## Start the App
1. Run: python src/app.py
2. Open: http://127.0.0.1:5000
