from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^&', views.article),
    # re_path('list/<year>',views.article_list),
    # re_path('list/month/<year>',views.article_list),
    re_path(r'^list/(?P<year>\d{4})/', views.acticle_list),
    re_path(r'^list/(?P<month>\d{2})/', views.acticle_list)
]
