from django.db import models


class Mobile(models.Model):
    mobile_no = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    is_verified = models.CharField(max_length=5)
    created_at = models.CharField(max_length=30)
    updated_at = models.CharField(max_length=30)