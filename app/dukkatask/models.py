# yourapp/models.py
from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=255)  # Consider using Django's built-in User model
