from django.contrib import admin
from django.urls import path
from . import views

app_name = 'front'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='signin'),
    path('detail/<artical_id>/<p>', views.login, name='signin'),
]
