from django import forms
from . tasks import send_expert_advice_email_task

class ExpertAdviceForm(forms.Form):
    name = forms.CharField(required=True, label='Your Name')
    phone_number = forms.CharField(required=True, label='Phone Number')
    email = forms.EmailField(required=True, label='Email Address')


    def send_email(self):
        send_expert_advice_email_task.delay(
            name = self.cleaned_data['name'],
            phone_number = self.cleaned_data['phone_number'],
            email = self.cleaned_data['email']
        )