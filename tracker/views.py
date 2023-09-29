from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookDetailInputForm

def index_page(request):
    if(request.method)== "POST":
        form = BookDetailInputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/all-books")
    else:
        form = BookDetailInputForm()
    return render(request, "tracker/index.html", {
        "form": form
    })


def all_books_page(request):
    all_books = Book.objects.all()
    return render(request, "tracker/all_books.html", {
        "books_info" : all_books
    })
