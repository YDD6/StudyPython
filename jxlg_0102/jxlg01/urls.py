from django.urls import path
from . import views
urlpatterns = [
    path('',views.book),
    path('detail/<book_id>/<category_id>',views.books_detail),
]