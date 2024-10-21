from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import messages
from . forms import UserRegistrationForm, ProfileEditForm, UserEditForm, OneTimePasswordForm, PasswordResetEmailForm
from . forms import  OneTimePasswordResetForm, CustomPasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Profile
from django.contrib.auth.models import User
from user_agents import parse
from . tasks import send_login_email_task

# Create your views here.

# User Registration
def user_registration(request):
    if request.user.is_authenticated:
        return redirect('user_languages_view')
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():

            # Cheking if Email already Exists
            email = registration_form.cleaned_data['email']
            if User.objects.filter(email = email):
                messages.error(request, "Email is already registered. Please use a different email.")
                return redirect('user_registration')

            otp = registration_form.send_email()
            request.session['registration_data'] = registration_form.cleaned_data
            request.session['registration_otp'] = otp

            return redirect('registration_otp_validate')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'Users/Registration.html', {'registration_form': registration_form} )

# Registration OTP
def registration_otp_validate(request):
    if request.user.is_authenticated:
        return redirect('user_languages_view')
    if request.method == 'POST':
        otp_form = OneTimePasswordForm(request.POST)
        if otp_form.is_valid():
            entered_otp = otp_form.cleaned_data['otp']
            session_otp = request.session.get('registration_otp')

            # Checking OTP is correct or not
            if entered_otp == session_otp:
                registration_data = request.session.get('registration_data')
                # If registration data is there creating user
                if registration_data:
                    user = User.objects.create_user(
                        first_name = registration_data['first_name'],
                        last_name = registration_data['last_name'],
                        username = registration_data['username'],
                        email = registration_data['email'],
                        password= registration_data['password1']
                    )
                    # Clearing session data
                    request.session.pop('registration_data', None)
                    request.session.pop('registration_otp', None)
                    return redirect('user_login')
                else:
                    messages.error(request, 'Registration data not found.')
            else:
                otp_form.add_error(None, 'Invalid OTP. Please try Again')
    else:
        otp_form = OneTimePasswordForm()
    return render(request, 'Users/registration_otp.html', {'otp_form' : otp_form})


# User Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_languages_view')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            # Login Mail
            current_user = user.username
            user_email   = user.email

            user_agent_string = request.META.get('HTTP_USER_AGENT','')
            user_agent = parse(user_agent_string)

            # Browser and Device
            browser = user_agent.browser.family
            browser_version = user_agent.browser.version_string
            os = user_agent.os.family
            device = user_agent.device.family

            # IP Address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            # Email Sending
            send_login_email_task.delay(
                username = username,
                email =user_email,
                browser = browser,
                browser_version = browser_version,
                os = os,
                device = device,
                ip = ip

            )
            
            return redirect('user_languages_view')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('user_login')
        
    return render(request, 'Users/Login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('/')


# Forgot Password
def forgot_password(request):
    if request.method == 'POST':
        email_form = PasswordResetEmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                otp = email_form.send_reset_password_email()
                request.session['email_data'] = email
                request.session['reset_otp'] = otp
                return redirect('password_reset_otp')
            except User.DoesNotExist:
                messages.error(request, "The email you entered doesn't have an associated account.")
    else:
        email_form = PasswordResetEmailForm()

    return render(request, 'Users/reset_password.html', {'email_form': email_form})

# Password Reset OTP
def password_reset_otp(request):
    if request.method == 'POST':
        otp_form = OneTimePasswordResetForm(request.POST)
        if otp_form.is_valid():
            entered_otp = otp_form.cleaned_data['otp']
            session_otp = request.session.get('reset_otp')

            # Checking if OTP is correct
            if entered_otp == session_otp:
                email_form_data = request.session.get('email_data')
                if email_form_data:
                    # Clear the OTP from the session
                    request.session.pop('reset_otp', None)
                    return redirect('password_reset_form')
                else:
                    messages.error(request, 'Email data not found.')
            else:
                otp_form.add_error(None, 'Invalid OTP. Please try again.')
    else:
        otp_form = OneTimePasswordResetForm()

    return render(request, 'Users/password_reset_otp.html', {'otp_form': otp_form})

# Password Reset Form
def password_reset_form(request):
    email = request.session.get('email_data')
    if not email:
        return redirect('user_login')
    user = get_object_or_404(User, email = email)

    if request.method == 'POST':

        password_form = CustomPasswordResetForm(user=user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
                            
            # Clear session data
            request.session.pop('email_data', None)     
            return redirect('user_login')

        else:
            password_form.add_error('new_password2', 'Passwords do not match.')
    else:
        password_form = CustomPasswordResetForm(user=user)

    return render(request, 'Users/password_reset_form.html', {'password_form': password_form})


# User Profile View
@login_required(login_url='/error_404/')
def profile_view(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'Users/Profile.html', {'user_profile' : user_profile})

# User Profile Edit
@login_required(login_url='/error_404/')
def profile_edit_details(request):
    user_profile = get_object_or_404(Profile, user= request.user)
    current_user = request.user
    if request.method == 'POST':
        profile_edit_form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)
        user_edit_form  = UserEditForm(request.POST, request.FILES, instance=current_user)
        if profile_edit_form.is_valid() and user_edit_form.is_valid():
            profile_edit_form.save()
            user_edit_form.save()
            return redirect('profile_view')
    else:
        profile_edit_form = ProfileEditForm(instance=user_profile)
        user_edit_form = UserEditForm(instance=current_user)

    context = {
        'profile_edit_form' : profile_edit_form,
        'user_edit_form' : user_edit_form

    }
    return render(request, 'Users/Profile_Edit_Details.html', context)

