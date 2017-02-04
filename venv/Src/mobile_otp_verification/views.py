from django.shortcuts import render
from .forms import OtpForm
from django.http import HttpResponse


def index(request):
    # Get url parameters mobile and otp number
    mobile_number = request.GET.get('mobile_number')
    otp = request.GET.get('otp')

    # Post request.
    # Check whether user has entered the otp number. If entered then generate a response by calling otp_verifier.
    if otp != "??????":

        # create a form instance and populate it with data from the request.
        form = OtpForm(request.POST)

        # check whether it's valid and then generate a response.
        return HttpResponse(form.otp_verifier(mobile_number, otp))

    # Get request.
    # if not then call mobile_otp_verification page so that user can enter otp number.
    elif otp == "??????":
        form = OtpForm()
        return render(request, 'mobile_otp_verification.html', {'form': form, 'mobile_number': mobile_number,
                                                                'otp': otp})