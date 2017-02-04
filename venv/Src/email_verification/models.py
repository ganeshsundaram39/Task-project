from django.db import models


class Email(models.Model):
    email_id = models.CharField(max_length=30)
    encrypted_email_id = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=100)
    is_verified = models.CharField(max_length=5)
    created_at = models.CharField(max_length=30)
    updated_at = models.CharField(max_length=30)