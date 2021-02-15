from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

class SearchForm(forms.Form):
    keyword = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Enter search term here',
                'class' : 'form-control'
            }
        )
    )