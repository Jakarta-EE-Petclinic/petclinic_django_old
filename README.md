# django_petclinic

* https://medium.com/@diwassharma/starting-a-python-django-project-on-mac-os-x-c089165cf010

```
brew install python3
python3 --version
sudo pip3 install virtualenv
virtualenv venv -p python3
source venv/bin/activate
deactivate
pip install Django==2.x.x
django-admin.py startproject project1
python manage.py runserver
```
# django_tutorial

## Tutorial

* https://docs.djangoproject.com/en/2.2/intro/tutorial01/
* https://docs.djangoproject.com/en/2.2/intro/tutorial02/
* https://docs.djangoproject.com/en/2.2/intro/tutorial03/
* https://docs.djangoproject.com/en/2.2/intro/tutorial04/
* https://docs.djangoproject.com/en/2.2/intro/tutorial05/
* https://docs.djangoproject.com/en/2.2/intro/tutorial06/
* https://docs.djangoproject.com/en/2.2/intro/tutorial07/

## Where do we go from here?
* https://docs.djangoproject.com/en/2.2/intro/whatsnext/
* https://docs.djangoproject.com/en/2.2/intro/reusable-apps/
* https://docs.djangoproject.com/en/2.2/contents/

## setup

* https://medium.com/@diwassharma/starting-a-python-django-project-on-mac-os-x-c089165cf010

### setup dev host

```
brew install python3
python3 --version
sudo pip3 install virtualenv
```

### setup project initial

```
virtualenv venv -p python3
source venv/bin/activate
deactivate
pip install Django==2.2.6
django-admin.py startproject django_tutorial
python manage.py startapp polls
python manage.py runserver
```

### setup project each time
```
source venv/bin/activate
python manage.py runserver
```


## setup IDE 
* https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-django-project.html
