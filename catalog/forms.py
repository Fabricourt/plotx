from django import forms
from .models import Company, Contactus

class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ('name',  'email', 'mobile', 'header', 'message')