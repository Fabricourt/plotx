from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
    
from django import forms

class TruckloanPlotForm(forms.Form):
    """Form for a secretary to check and renew   the new installment ."""
    renewpayment_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewpayment_date(self):
        data = self.cleaned_data['renewpayment_date']
        
        # Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - payment set on a past'))
        # Check date is in range secretary allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - payment set more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data