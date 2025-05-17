from django import forms
from .models import Book, BookListing

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
            'image_url'
        ]
        
class BookListingForm(forms.ModelForm):
    class Meta:
        model = BookListing
        fields = ['book', 'condition', 'price', 'member_owner']
        widgets = {
            'book': forms.Select(attrs={
                'class': 'w-full border rounded-xl px-3 py-2'
            }),
            'condition': forms.Select(attrs={'class': 'w-full border rounded-xl px-3 py-2'}),
            'price': forms.NumberInput(attrs={
                'min': 0,
                'step': '0.01',
                'class': 'w-full border rounded-xl px-3 py-2'
            }),
            'member_owner': forms.HiddenInput(),
        }