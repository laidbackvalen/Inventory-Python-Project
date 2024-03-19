from django import forms
from .models import quer,quer1

class queryform(forms.ModelForm):
    class Meta:
        model = quer
        fields = '__all__'

class queryform2(forms.ModelForm):
    class Meta:
        model = quer1
        fields = '__all__'
