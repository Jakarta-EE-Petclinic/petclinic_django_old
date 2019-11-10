#!/usr/bin/env zsh


function setup() {
  sudo apt-get install python3-pip
  sudo pip3 install virtualenv
  virtualenv venv
  source venv/bin/activate
  pip3 install Django
  pip3 install psycopg2
  python3 manage.py createsuperuser
  python3 manage.py runserver
}






#source venv/bin/activate
python3 manage.py runserver
#deactivate

#python manage.py createsuperuser
