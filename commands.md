# Packages Used
    django
    python-dotenv (for .env file)
    djangorestframework
    pytest
    black (Python formatter keeping it indivigual)
    django-mptt ( to implement eficient query for Nested Relations)
    djangorestframework-simplejwt ( for JWT Authentication )
    djoser ( JWT login Logout password reset )
    django-cors-headers ( for Cros Origine Requests )
    pillow ( for images )
    django_filters ( for filtering )
    sslcommerz-lib  


# Commands
django-admin startproject project_name

./manage.py runserver

./manage.py runserver shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

pip install python-dotenv

pip install djangorestframework

pip install pytest

pip install django-mptt

pip install djangorestframework-simplejwt

pip install djoser

pip install django-cors-headers

python -m pip install Pillow

pip install django-filter

pip install sslcommerz-lib