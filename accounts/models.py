from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phonenumber = models.CharField(max_length=12, blank=True)
    is_admin= models.BooleanField('Is admin', default=False)
    is_agent = models.BooleanField('Is agent', default=False)