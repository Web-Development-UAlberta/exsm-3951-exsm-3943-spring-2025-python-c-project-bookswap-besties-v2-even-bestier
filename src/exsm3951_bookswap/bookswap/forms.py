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
            # 'book': '',
            'condition': forms.Select(attrs={'class': ''}),
            'price': forms.NumberInput(attrs={
                'min': 0,
                'step': '0.01'
            }),
            'member_owner': forms.HiddenInput(),
        }