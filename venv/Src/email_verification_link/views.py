from django.http import HttpResponse
from email_verification.crypto import decrypt_val
from email_verification.models import Email
from time import gmtime, strftime


# Create your views here.
def index(request):
    try:
        encrypted_email_id=request.GET.get('encrypted_email_id')
        verification_code=request.GET.get('verification_code')
        email_id = decrypt_val(encrypted_email_id)
        if Email.objects.filter(email_id=email_id).count() == 1:
            if Email.objects.filter(verification_code=verification_code).count() == 1:
                t = Email.objects.get(email_id=email_id)
                t.is_verified = 'true'
                t.updated_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                t.save()
                message = "Email Verified"
            else:
                message = "Email not verified, retry again by clicking the link..!!"

        else:
            message = "Email not found to be verified."

    except Exception as e:
        message = "Email not verified, retry again by clicking the link..!!"

    return HttpResponse(message)