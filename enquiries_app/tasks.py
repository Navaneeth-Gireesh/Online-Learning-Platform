from celery import shared_task
from celery.utils.log import get_task_logger
from .email import send_expert_advice_email

logger = get_task_logger(__name__)

@shared_task(name='send_expert_advice_email_task', bind=True)
def send_expert_advice_email_task(self, name, phone_number, email):
    logger.info("Sending expert advice email")
    return send_expert_advice_email(name = name, phone_number = phone_number ,email = email)