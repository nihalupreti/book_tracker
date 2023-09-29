from django import forms
from .models import Book

# class BookDetailInputForm(forms.Form):
#     book_name = forms.CharField()
#     author = forms.CharField()
#     genre = forms.CharField()
#     rating = forms.CharField()

#     def __init__(self, *args, **kwargs):
#         kwargs["label_suffix"] = ""
#         super().__init__(*args, **kwargs)

class BookDetailInputForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"