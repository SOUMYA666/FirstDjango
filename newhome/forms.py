from django import forms
from newhome.models import Book,Author,Genre


class BookForms(forms.Form):
    name=forms.CharField(label='Book Name',
        widget=forms.TextInput(attrs={'maxlength':'30','name':'name','id':'name','placeholder':'Name of Book','class':'form-control'}))

    author=forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label='Author',
        widget=forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))

    purchase_date=forms.DateField(label='',
         widget=forms.DateInput(attrs={'placeholder':'Purchase Date','name':'purchase_date','id':'purchase_date','class':'form-control'}))

    #isbn=forms.CharField(label='ISBN Number',
        #widget=forms.TextInput(attrs={'placeholder':'ISBN Number','name':'isbn','id':'isbn','class':'form-control'}))

    # genre=forms.ModelMultipleChoiceField(
    #     queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)




class ModelBookForms(forms.ModelForm):
    title=forms.CharField(label='BookName',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Name of Book','class':'form-control'}))

    author=forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label='Author',
        widget=forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))

    summary=forms.CharField(label='Summary',
        widget=forms.Textarea(attrs={'placeholder':'Summary','name':'summary','id':'summary','class':'form-control'}))

    isbn=forms.CharField(label='ISBN Number',
        widget=forms.TextInput(attrs={'placeholder':'ISBN Number','name':'isbn','id':'isbn','class':'form-control'}))

    genre=forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        
        widget=forms.CheckboxSelectMultiple)

class Meta:
        model = Book #This is dependency injection here no need to craete object of class
        #model=Book,Genre
        #fields = '__all__'
        fields = ('name','genre','purchase_date','author')
        #fields = ('title','author','summary')

#widget=forms.TextInput(attrs={})

class SearchForm(forms.Form):
    q = forms.CharField(label = '',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Search','class':'form-control', 'minlength':'2'}))
