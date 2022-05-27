from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    phone = models.TextField(name=('PhoneNumber'), max_length=13)
    birthday = models.TextField(name=('BirthdayDate'))
    tryBalance = models.FloatField(name=('TRYBalance') , default=0)
    usdBalance = models.FloatField(name=('USDBalance') , default=100000)
    euroBalance = models.FloatField(name=('EURBalance') , default=0)