import time
from django.core.mail import send_mail
from django.conf import settings


def run_this_function():
    print("Function Started:")
    print("Function Started..")

    time.sleep(2)
    print("Function Executed")


def send_email_to_client():
    subject = "This is email is from django server"
    message = "This is a test message from django server email"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["connecthassan76@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)

