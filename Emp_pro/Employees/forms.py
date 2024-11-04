from django import forms
from .models import Emp

class Empform(forms.ModelForm):
    class Meta:
        model=Emp
        fields=["name","email","department","role"]