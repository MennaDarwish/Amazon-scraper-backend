# jungle-scout-task-BE


This repository contains the server for scraping amazon data

## Getting started

Clone the repository

```
git clone https://github.com/MennaDarwish/jungle-scout-task-BE.git
```

Set up and activate a python v3 environment

```
python3 -m venv env
source env/bin/activate
```

Install the required python libraries for local development

```
pip install -r requirements/local.txt
```

## Create the database tables
```
python manage.py migrate
```

## Run server
```
python manage.py runserver
```
