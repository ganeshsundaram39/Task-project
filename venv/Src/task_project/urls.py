from django.conf.urls import url
from django.contrib import admin
from . import views
from email_verification import views as email_verification_view
from email_verification_link import views as email_verification_link_view
from sms_verification import views as sms_verification_view
from mobile_otp_verification import views as mobile_otp_verification_view


urlpatterns = [
    url(r'^email_verification/',email_verification_view.index),
    url(r'^email_verification_link/', email_verification_link_view.index),
    url(r'^sms_verification/', sms_verification_view.index),
    url(r'^mobile_otp_verification',mobile_otp_verification_view.index),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index)
]
