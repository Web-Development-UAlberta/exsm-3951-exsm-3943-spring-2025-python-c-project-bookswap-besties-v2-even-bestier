from django.contrib.auth.forms import UserCreationForm
from django import forms
from authentication.models import Member

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