from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_page),
    path("all-books", views.all_books_page)
]
