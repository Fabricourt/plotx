from django import forms
from .models import Contactk, Contact, Contactchurch

class ContactkForm(forms.ModelForm):
    class Meta:
        model = Contactk
        fields = (
            'user_id', 
            'name',
            'email',
            'phone',
            'header',
            'message',
            )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'business',
            'business_id',
            'user_id', 
            'name',
            'email',
            'phone',
            'header',
            'message',
            )
    
class ContactchurchForm(forms.ModelForm):
    class Meta:
        model = Contactchurch
        fields = (
            'church',
            'church_id',
            'user_id', 
            'name',
            'email',
            'phone',
            'header',
            'message',
            )
    