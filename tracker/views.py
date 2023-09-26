from django.shortcuts import render
from .models import Book

def index_page(request):
    return render(request, "tracker/index.html")


def all_books_page(request):
    all_books = Book.objects.all()
    return render(request, "tracker/all_books.html", {
        "books_info" : all_books
    })
