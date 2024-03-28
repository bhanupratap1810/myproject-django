from django.db import models

class OTP(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)  # Adjust max length as per requirements
    email_otp_code = models.CharField(max_length=6)
    mobile_otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.phone_number}"
