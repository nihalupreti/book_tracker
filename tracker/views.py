from django.shortcuts import render
from .models import Book
from .forms import BookDetailInputForm

def index_page(request):
    if(request.method)== "POST":
        user_input = request.POST
        book_database = Book.objects.create(title=user_input["book_name"],author=user_input["author"],genre=user_input["genre"],rating=int(user_input["rating"]))
    form = BookDetailInputForm()
    return render(request, "tracker/index.html", {
        "form": form
    })


def all_books_page(request):
    all_books = Book.objects.all()
    return render(request, "tracker/all_books.html", {
        "books_info" : all_books
    })
