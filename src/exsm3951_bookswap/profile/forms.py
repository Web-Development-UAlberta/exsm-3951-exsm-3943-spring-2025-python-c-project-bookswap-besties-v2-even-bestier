from django.contrib.auth.forms import UserCreationForm
from django import forms
from authentication.models import Member


class CustomEditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomEditUserForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            attrs = {
                'class': 'block w-auto min-w-[200px] max-w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200',
                'id': field_name,
                'placeholder': f'Enter {field.label}'
            }
            
            if isinstance(field.widget, forms.Textarea):
                attrs['rows'] = '1'
                attrs['style'] = 'resize: vertical;'
            
            if field_name == 'address' and isinstance(field.widget, forms.Textarea):
                attrs['rows'] = '4'
                attrs['style'] = 'resize: vertical;'

            field.widget.attrs.update(attrs)


    class Meta:
        model = Member
        fields = ["username", "email", "first_name", "last_name", "address", "genre_preference"]
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address': 'Address',
            'genre_preference': 'Genre',
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
