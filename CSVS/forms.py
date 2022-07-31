from pyexpat import model
from django import forms
from .models import Csv

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ['file_name']