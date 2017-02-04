from django import forms
import random
from sms_verification.models import Mobile
from time import gmtime, strftime
from sendsms import api
import webbrowser


class SmsForm(forms.Form):

    # Declare textbox with label that takes mobile number.
    mobile_no = forms.CharField(label='Your mobile number:', max_length=10, min_length=10)

    # Method that validates mobile number, checks database for number then inserts or delete and then sends message.
    def sms_verifier(self):

        # Get number from the textbox.
        mobile_no = self.cleaned_data["mobile_no"]

        # Validation.
        if len(mobile_no) == 10:
            # Random number generator.
            random_number = random.randint(100000, 999999)
            # Get date and time.
            datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

            # Check database if number is found update.
            if Mobile.objects.filter(mobile_no=mobile_no).count() == 1:
                update = Mobile.objects.get(mobile_no=mobile_no)
                update.is_verified = 'false'
                update.updated_at = ''
                update.created_at = datetime
                update.save()
            # else insert.
            elif Mobile.objects.filter(mobile_no=mobile_no).count() != 1:
                insert = Mobile(mobile_no=mobile_no, otp=random_number, is_verified="false", created_at=datetime,
                                updated_at="")
                insert.save()

            # Send Sms to user. Since Sms is not free message will be printed in the console.
            api.send_sms(body='Dear sir,\nYour OTP number is {}.\nThank you.'.format(random_number),
                         from_phone='+919999999999' , to=[mobile_no])
            message = ""

            # Open new page and call mobile_otp_verification and pass parameter.
            webbrowser.open('http://127.0.0.1:8000/mobile_otp_verification?mobile_number='+mobile_no+'&otp=??????',
                            new=1,autoraise=False)
        else:
            message = "Mobile number not valid"

        return message
