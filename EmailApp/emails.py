from __future__ import absolute_import

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_review_email(name, email_address, email_subject, review_message):

    context = {
        'name' : name,
        'email' : email_address,
        'review_message' : review_message,
    }

    email_body = render_to_string('EmailApp/email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email_address, ],
    )

    return email.send(fail_silently=False)