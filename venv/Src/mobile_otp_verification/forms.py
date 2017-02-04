from django import forms
from sms_verification.models import Mobile
from time import gmtime, strftime


class OtpForm(forms.Form):
    # Textbox with label that takes OTP number from user
    otp_no = forms.CharField(label='Enter OTP number:', max_length=6, min_length=6)

    def otp_verifier(self,mobile_number,otp):
        # Check mobile number is valid.
        if Mobile.objects.filter(mobile_no=mobile_number).count() == 1:
            # Check OTP number is valid.
            if Mobile.objects.filter(otp=otp).count() == 1:
                # Get reference to the row in database
                t = Mobile.objects.get(mobile_no=mobile_number)
                t.is_verified = 'true'
                t.updated_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                t.save()
                message = "Mobile number Verified"
            else:
                message = "Mobile number not Verified, Retry"

        else:
            message = "Mobile number not found to be verified."

        return message

