# Amazon-scraper-backend


This repository contains the server for scraping amazon data

## Getting started

Clone the repository

```
https://github.com/MennaDarwish/Amazon-scraper-backend.git
```

Set up and activate a python v3 environment

```
python3 -m venv env
source env/bin/activate
```

Install the required python libraries for local development

```
pip install -r requirements.txt
```

## Create the database tables
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Run server
```
python manage.py runserver
```
