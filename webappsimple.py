import os
webappname = os.path.basename(__file__)[0:-3]
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', webappname)
    import django.core.management
    django.core.management.execute_from_command_line([ '', 'runserver' ])
SECRET_KEY = 'secret'
ROOT_URLCONF = webappname
WSGI_APPLICATION = webappname + '.application'
import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()

DEBUG = True
#ALLOWED_HOSTS = [ "localhost" ]

# webapp main
from django.http import HttpResponse
from django.shortcuts import redirect, render

def root(req):
    return HttpResponse("<h1>simple django</h1>")

from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('', root),
]
