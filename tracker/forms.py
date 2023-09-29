from django import forms

class BookDetailInputForm(forms.Form):
    book_name = forms.CharField()
    author = forms.CharField()
    genre = forms.CharField()
    rating = forms.CharField()

    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

