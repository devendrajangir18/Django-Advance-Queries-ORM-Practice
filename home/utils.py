from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "This email is from Django server"
    message = "This email is for testing purpose"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [""]
    send_mail(subject , message , from_email , recipient_list)
