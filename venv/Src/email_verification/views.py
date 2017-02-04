from django.shortcuts import render
from .forms import EmailForm


def index(request):
    # if this is a POST request we need to process the form data
    message = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            message = form.email_verifier()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'email_verification.html', {'form': form, 'message': message})