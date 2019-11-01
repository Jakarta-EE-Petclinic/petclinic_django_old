#!/usr/bin/env bash

sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate


# https://github.com/jieter/django-tables2
# https://django-tables2.readthedocs.io/en/latest/pages/installation.html
pip install django-tables2
pip install django-debug-toolbar
pip install django-extensions
pip install django-allauth
pip install django-crispy-forms
pip install django-crispy-forms
pip install django-generic-scaffold
pip install django-import-export


#pip install django-compressor