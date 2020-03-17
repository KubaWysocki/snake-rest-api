# snake-rest-api
Rest API for snake game 

## Usage (on linux)
- download project
- create venv and use it with `source ./venv/bin/activate`
- change directory to /rest-api
- `pip install requirements.txt`
- `python manage.py runserver 0.0.0.0:8000`

Now you can start using django admin panel

or

you can download [this](https://github.com/KubaWysocki/Snake) project and see whole app running

## Features
- creating user accounts with username and encrypted password
- creating records that contain game mode and score information
- returning information about achieved highscore
- returning scoreboards with records

## Tech stack
- django
- django-rest-framework
- simplejwt

