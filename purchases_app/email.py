
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from celery.utils.log import get_task_logger
from courses_app.models import Course
from django.contrib.auth.models import User

logger = get_task_logger(__name__)


def send_course_purchase_email(email, language, course_category, course):
    selected_user       = User.objects.get(email = email)
    selected_course     = Course.objects.get(title = course)
    thumbnail           = selected_course.thumbnail
    context = {
        'selected_user'             : selected_user,
        'email'                     : email,
        'language'                  : language,
        'course_category'           : course_category,
        'course'                    : course,
        'thumbnail'                 : thumbnail  
    }

    email_subject = 'EduSphere Course Purchase Email'
    email_body = render_to_string('Users/Couse_Purchase_Email_Message.html', context)

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
        logger.error(f'Failed to send Course Purchase Email to {email}: {e}')
        return False
    