from django.shortcuts import render
from .forms import SmsForm


def index(request):
    # if this is a POST request we need to process the form data
    message = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SmsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            message = form.sms_verifier()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SmsForm()

    return render(request, 'sms_verification.html', {'form': form, 'message': message})