#!/usr/bin/env bash


function setup() {
  sudo apt-get install python3-pip
  sudo pip3 install virtualenv
  virtualenv venv
  source venv/bin/activate
  pip3 install Django
  pip3 install psycopg2
  python3 manage.py runserver
  python3 manage.py createsuperuser
  python3 manage.py runserver
}

function shell() {
  source venv/bin/activate
  python3 manage.py shell
  deactivate
}

function update_model() {
  source venv/bin/activate
  python3 manage.py makemigrations
  python3 manage.py migrate
  deactivate
}

function run_docker() {
  docker-compose -f stack.yml up
}

function runserver() {
  source venv/bin/activate
  python3 manage.py runserver
  deactivate
}

runserver

