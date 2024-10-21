from celery import shared_task
from celery.utils.log import get_task_logger
from . email import send_otp_email, send_reset_password_otp_email, send_account_update_email, send_login_account_email

logger = get_task_logger(__name__)


@shared_task(name = 'send_otp_email_task', bind=True)
def send_otp_email_task(self,first_name,last_name,email,otp):
    logger.info(f"Sending OTP to Email {email} ...")
    success = send_otp_email(first_name=first_name, last_name=last_name, email=email, otp=otp)

    if not success:
        logger.info(f"OTP Sending Failed to {email} ...")
    return success


@shared_task(name = 'send_reset_otp_email_task', bind=True)
def send_reset_otp_email_task(self, email, otp):
    logger.info(f"Sending Reset Password OTP to Email {email} ...")
    success = send_reset_password_otp_email(email=email, otp = otp)

    if not success:
        logger.info(f"OTP Sending Failed to {email} ...")
    return success


@shared_task(name = 'send_account_update_email_task', bind=True)
def send_account_update_email_task(self, username, email, active, teacher, admin):
    logger.info(f"Sending Account Update Email to {email} ...")
    success = send_account_update_email(username = username, email = email, active = active, teacher = teacher, admin = admin)
    
    if not success:
        logger.info(f"Sending Account Update Email failed to {email} ...")
    return success

@shared_task(name = 'send_login_email_task', bind=True)
def send_login_email_task(self, username, email, browser, browser_version, os, device, ip):
    logger.info(f"Sending Account Login Email to {email} ...")
    success = send_login_account_email(username = username, email = email, browser = browser, browser_version = browser_version, os = os, device = device, ip = ip)
    
    if not success:
        logger.info(f"Sending Account login Email Message failed to {email} ...")
    return success
