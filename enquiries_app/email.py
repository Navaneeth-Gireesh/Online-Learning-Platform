from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

def send_expert_advice_email(name, email, phone_number):

    context = {
        'name' : name,
        'phone_number' : phone_number,
        'email': email,
    }

    email_subject = 'Confirmation of Your Free Consultation Request'
    email_body = render_to_string('email_message.html', context)


    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL, [email, 'navaneeth2002hitech@gmail.com']
    )
    try:
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        return True
    except Exception as e:
        logger.error(f'Failed to send Consultaion Email to {email}: {e}')
        return False