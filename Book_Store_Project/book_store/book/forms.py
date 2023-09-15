from django import forms
from book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        # fields = '__all__'
        exclude = ['first_published','last_published']
        
        
        