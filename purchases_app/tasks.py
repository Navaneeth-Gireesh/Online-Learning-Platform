from celery import shared_task
from celery.utils.log import get_task_logger
from . email import send_course_purchase_email

logger = get_task_logger(__name__)


@shared_task(name='send_course_purchase_email_task', bind=True)
def send_course_purchase_email_task(self, email, language, course_category, course):
    logger.info(f"Sending Course Purchase Email to {email} ...")
    success = send_course_purchase_email(

        email=email,
        language=language,
        course_category=course_category,
        course=course
    )

    if not success:
        logger.info(f"OTP Sending Failed to {email} ...")
    return success
