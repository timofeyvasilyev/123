"""
URL configuration for progi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from progi.views import IndexView
from progi.views import get_students, send_data, delete_data
from model import db

urlpatterns = [
    path('get-students/',  get_students, name='get-students'),
    path('set-student/',  send_data, name='set-student'),
    path('delete-student/',  delete_data, name='delete-student'),
    path('admin/', admin.site.urls),
    path('',  IndexView.as_view()),
]
