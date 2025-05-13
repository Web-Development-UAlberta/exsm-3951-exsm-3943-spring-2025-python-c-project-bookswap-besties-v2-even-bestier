from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'isbn',
            'title',
            'author',
            'genre',
            'description',
            'pub_date',
            'language',
            'weight',
        ]