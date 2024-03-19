from django import forms
from adminprofile.models import items
class ItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = '__all__'