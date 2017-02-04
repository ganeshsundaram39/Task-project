# -*- coding: utf-8 -*-
from django import forms
import re
from email_verification.models import Email
from crypto import encrypt_val
from django.utils.crypto import get_random_string
from time import gmtime, strftime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class EmailForm(forms.Form):
    your_email = forms.CharField(label='Your Email:', max_length=30)

    def email_verifier(self):
        # get value from the textbox and store it in the email_id
        email_id = self.cleaned_data["your_email"]
        email_regex = re.compile(r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
                                 r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'
                                 r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)

        if not email_regex.match(email_id) or email_id == "mandummy89@gmail.com":
            message = "Email-id not valid"
        else:
            verification_code = get_random_string(length=32)
            encrypted_email_id = encrypt_val(email_id)
            datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            if Email.objects.filter(email_id=email_id).count() == 1:
                update = Email.objects.get(email_id=email_id)
                update.is_verified = 'false'
                update.updated_at = ''
                update.created_at = datetime
                update.encrypted_email_id = encrypted_email_id
                update.verification_code = verification_code
                update.save()
            elif Email.objects.filter(email_id=email_id).count() != 1:
                insert = Email(email_id=email_id,  encrypted_email_id=encrypted_email_id,
                               verification_code=verification_code,
                               is_verified="false", created_at=datetime, updated_at="")
                insert.save()

            href = 'encrypted_email_id='+encrypted_email_id+u'&verification_code='+verification_code
            html_content = u'<p>Dear Sir, <br/><br/>Thank you for registering.<br/> As next step, please click' \
                           u' <a href="http://127.0.0.1:8000/email_verification_link?'+href+u'" target="_blank">Link</a>' \
                           u' to verify your email address.<br/><br/>Many thanks,<br/>Ganesh Sundaram.</p>'
            msg = EmailMultiAlternatives('Verification link for your Email registration', '', settings.EMAIL_HOST_USER, [email_id])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            message = "We now need to verify your email address. We've sent an email to "+email_id+" to verify your address. " \
                      "Please click the link in that email to continue. "

        return message
