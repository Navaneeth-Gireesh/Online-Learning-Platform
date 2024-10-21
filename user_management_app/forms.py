from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import Profile
import random
from .tasks import send_otp_email_task ,send_reset_otp_email_task


def random_otp():
    return random.randint(100000, 999999)
# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    usable_password = None
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }

    def send_email(self):
        otp = random_otp()  
        send_otp_email_task.delay(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            otp=otp
        )
        return otp
        
# Registration OTP Form
class OneTimePasswordForm(forms.Form):  
    otp = forms.IntegerField(max_value=999999, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter OTP'}))

# Reset Password Email
class PasswordResetEmailForm(forms.Form):
    email = forms.EmailField(required=True)

    def send_reset_password_email(self):
        otp = random_otp()  
        send_reset_otp_email_task.delay(
            email=self.cleaned_data['email'],
            otp=otp
        )
        return otp

# Reset Password OTP
class OneTimePasswordResetForm(forms.Form):
    otp = forms.IntegerField(max_value=999999, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter OTP'}))
# Password Reset Form
class CustomPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New password'}),
        label='New password'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}),
        label='Confirm new password'
    )

# Profile Edit Form
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 
            'mobile_number', 
            'date_of_birth', 
            'language',
            'location', 
            'gender', 
            'education', 
            'occupational_status'
        ]
        labels = {
            'profile_picture': 'Profile Picture',
            'mobile_number': 'Mobile Number',
            'date_of_birth': 'Date Of Birth',
            'language':'Language',
            'location': 'Location',
            'gender': 'Gender',
            'education': 'Education',
            'occupational_status': 'Occupation'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }



# User Data Edit Form
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email Address',
        }

        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled'})
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True 

