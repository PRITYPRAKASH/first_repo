from dataclasses import fields
from django import forms
from .models import  csvs

class csvsModelform(forms.ModelsForm):
    class Meta:
        model=csvs
        fields=("file_name",)