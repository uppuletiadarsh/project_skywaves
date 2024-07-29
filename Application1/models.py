
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)  # Assuming mobile number is stored as a string
    email = models.EmailField(unique=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    password = models.CharField(max_length=100)
