from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('wuwang/', views.login, name='signin'),
]
