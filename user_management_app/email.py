
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


def send_otp_email(first_name,last_name,email,otp):
    context = {
        'first_name'    : first_name,
        'last_name'     : last_name,
        'email'         : email,
        'otp'           : otp  
    }

    email_subject = 'EduSphere Account Registration OTP'
    email_body = render_to_string('Users/register_otp_email_message.html', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL, [email]
    )
    try:
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        return True
    except Exception as e:
        logger.error(f'Failed to send OTP Email to {email}: {e}')
        return False
    
def send_reset_password_otp_email(email, otp):
    context = {
        'email' : email,
        'otp'   : otp
    }
    email_subject = 'EduSphere Account Password Reset OTP'
    email_body = render_to_string('Users/password_reset_otp_email_message.html', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL, [email]
    )
    try:
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        return True
    except Exception as e:
        logger.error(f'Failed to send Reset OTP Email to {email}: {e}')
        return False
    

def send_account_update_email(username, email, active, teacher, admin):
    context = {
        'username'  : username,
        'email'     : email,
        'active'    : active,
        'teacher'   : teacher,
        'admin'     : admin

    }
    email_subject = 'EduSphere Account Updation'
    email_body = render_to_string('Admins/User_Update_Email_Message.html', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL, [email]
    )
    try:
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        return True
    except Exception as e:
        logger.error(f'Failed to send Email to {email}: {e}')
        return False
    

def send_login_account_email(username, email, browser, browser_version, os, device, ip):
    context = {
        'username'          : username,
        'email'             : email,
        'browser'           : browser,
        'browser_version'   : browser_version,
        'os'                : os,
        'device'            : device,
        'ip'                : ip

    }
    email_subject = 'EduSphere Account - Security Login Alert'
    email_body = render_to_string('Users/User_Account_Login_Email_Message.html', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL, [email]
    )
    try:
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        return True
    except Exception as e:
        logger.error(f'Failed to send Email to {email}: {e}')
        return False