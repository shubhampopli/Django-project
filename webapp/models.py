from django.db import models

# Create your models here.

class employees(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=10)
    email=models.CharField(max_length=250, null=True)
    emp_id=models.IntegerField()

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)