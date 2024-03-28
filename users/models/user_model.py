from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=128)
    business_in_us = models.BooleanField(default=False)

    def set_password(self, password):
        self.password_hash = make_password(password)

    def __str__(self):
        return self.email
