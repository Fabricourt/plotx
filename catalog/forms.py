from django import forms
from .models import Company, Plot

class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = '__all__'

