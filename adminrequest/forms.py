from django import forms
from .models import approval

class approvalform(forms.ModelForm):
    class Meta:
        model = approval
        fields = '__all__'
