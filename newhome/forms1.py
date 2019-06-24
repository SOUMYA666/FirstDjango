from django import forms
from newhome.models import Book, Author, Library

class BookForms(forms.Form):
    title = forms.CharField(label='name',
            widget = forms.TextInput(attrs={'maxlength':'30', 'placeholder': 'Book Name', 'class':'form-control'}))
    author = forms.ModelChoiceField(
        queryset = Author.objects.all(),
        empty_label='Author',widget=forms.Select(attrs={'name': 'author','id': 'author','class':'custom-select'}))
    purchase_date=forms.DateField(label='',
                    widget= forms.DateInput(attrs={'placeholder': 'purchase_date', 'name':'purchase_date',
                    'id': 'purchase_date', 'class':'form-control'}))


class ModelBookForms(forms.ModelForm):
    title = forms.CharField(label='Book Name',
        widget = forms.TextInput(attrs={'maxlength':'30', 'placeholder': 'Book Name', 'class':'form-control'}))
    author = forms.ModelChoiceField(
        queryset = Author.objects.all(),
        empty_label='Author',widget=forms.Select(attrs={'name': 'author','id': 'author','class':'custom-select'}))
    genre = forms.ModelMultipleChoiceField(queryset=Library.objects.all(),
                widget= forms.CheckboxSelectMultiple)
    purchase_date=forms.DateField(label='',
                    widget= forms.DateInput(attrs={'placeholder': 'purchase_date', 'name':'purchase_date',
                    'id': 'purchase_date', 'class':'form-control'}))


class Meta:
    model = Book
    fields = '__all__'
    
#127.0.0.1:8000/form/name=name&password=acd@123