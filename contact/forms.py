from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'company',
            'company_id',
            'user_id', 
            'name',
            'email',
            'phone',
            'header',
            'message',
            )
    