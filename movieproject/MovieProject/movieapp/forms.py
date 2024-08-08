from django import forms
from . models import movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','img']

def clean(self):
    cleaned_data=super().clean