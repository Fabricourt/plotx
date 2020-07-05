from .models import Answer
from django import  forms

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ( 
            'file_name',
            'answers',
            'name',
            )