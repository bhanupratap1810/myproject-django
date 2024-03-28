from django.core.mail import send_mail
from django.conf import settings

from ..utils import generate_otp_code

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client  # Assuming you're using Twilio for SMS
from users.models import OTP

@api_view(['POST'])
def generate_otp(request):
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')

    email_otp_code=generate_otp_code()
    mobile_otp_code = generate_otp_code()

    OTP.objects.create(email=email, phone_number=phone_number, email_otp_code=email_otp_code, mobile_otp_code=mobile_otp_code)

    # Send the OTP code to the user via email
    send_email_otp(email, email_otp_code)

    # Send the OTP code to the user via SMS
    send_sms_otp(phone_number, mobile_otp_code)

    return Response({'message': 'OTP generated successfully'}, status=status.HTTP_201_CREATED)

def send_email_otp(email, otp_code):
    subject = 'Your OTP Verification Code'
    message = f'Your OTP code is: {otp_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_sms_otp(phone_number, otp_code):
    # Replace these placeholders with your actual Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your OTP code is: {otp_code}',
        from_=twilio_phone_number,
        to=phone_number
    )

@api_view(['POST'])
def verify_otp(request):
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')
    email_otp_code = request.data.get('email_otp_code')
    mobile_otp_code = request.data.get('mobile_otp_code')

    if OTP.objects.filter(email=email, phone_number=phone_number, email_otp_code=email_otp_code, mobile_otp_code=mobile_otp_code).exists():
        return Response({'message': 'OTP verification successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)