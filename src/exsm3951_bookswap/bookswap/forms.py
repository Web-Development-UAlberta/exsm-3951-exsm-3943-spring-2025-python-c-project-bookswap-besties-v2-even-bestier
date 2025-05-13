from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Member, Book


class CustomEditUserForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ("username", "email", "first_name", "last_name", "address", "genre_preference")
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address': 'Address',
            'genre_preference': 'Genre',
        }

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