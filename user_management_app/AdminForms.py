from django import forms
from django.contrib.auth.models import User
from . tasks import send_account_update_email_task


class AdminUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'is_active',
            'is_staff',
            'is_superuser'
        ]
        labels = {
            'username'      : 'Username',
            'email'         : 'Email Address',
            'is_active'     : 'Active',
            'is_staff'      : 'Teacher',
            'is_superuser'  : 'Admin'
        }
    def __init__(self, *args, **kwargs):
        super(AdminUserEditForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

    def send_email(self):
        send_account_update_email_task.delay(
            username    = self.cleaned_data['username'],
            email       = self.cleaned_data['email'],
            active      = self.cleaned_data['is_active'],
            teacher     = self.cleaned_data['is_staff'],
            admin       = self.cleaned_data['is_superuser']
        )