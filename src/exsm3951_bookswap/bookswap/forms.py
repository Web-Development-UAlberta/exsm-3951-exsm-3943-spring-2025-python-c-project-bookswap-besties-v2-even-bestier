from django import forms
from .models import Book, BookListing, LibraryItem

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #set some fields to hidden
        hidden_fields = ['language', 'weight', 'image_url']
        for field_name in hidden_fields:
            self.fields[field_name].widget = forms.HiddenInput()

        
class BookListingForm(forms.ModelForm):
    class Meta:
        model = BookListing
        fields = ['library_item', 'condition', 'price', 'member_owner']
        widgets = {

            'library_item': forms.Select(attrs={
 
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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if self.user:
            self.fields['library_item'].choices = self.get_library_item_choices(self.user)
            
    def get_library_item_choices(self, user):
        choices = [(obj.id, str(obj)) for obj in LibraryItem.objects.filter(member=user)]
        return choices

