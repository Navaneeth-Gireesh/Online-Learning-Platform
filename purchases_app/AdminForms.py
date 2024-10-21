from django import forms
from . models import CouponCode

class CouponCodeForm(forms.ModelForm):
    class Meta:
        model = CouponCode
        fields = [
            'valid_to',
            'usage_limit'
        ]
        labels ={
            'valid_to' : 'Valid To',
            'usage_limit' : 'Usage Limit'
        }
        widgets = {
            'valid_to': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            }