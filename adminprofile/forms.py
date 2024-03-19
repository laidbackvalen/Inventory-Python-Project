from django import forms
from .models import returnmodel

class returnform(forms.ModelForm):
    class Meta:
        model = returnmodel
        fields = '__all__'
