#!/bin/sh
export FLASK_APP=./http_serv/index.py
export FLASK_RUN_PORT=8080
source pipenv --venv/bin/activate
flask run -h 0.0.0.0
