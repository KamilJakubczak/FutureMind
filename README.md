# FutureMind
This is example project for interview purpose, and it's written to run only locally. 

## How to start app

### Setting environment
Prepare .env file based on .env-example, keep the ENV variable as 'dev' or anything besides 'prod'
Note that based on ENV variable the database engine will be chosen, for prod will be PostgreSQL for dev SQLite

### Running with django server
Go to **backend/imageprocessor** directory then run`python manage.py runserver`

### Running with docker
Run `docker compose up` in main directory of repository

### Running tests
Set ENV variable to dev and run `pytest` in **backend/imageprocessor** directory
