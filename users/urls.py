from django.urls import path
from .views.auth_view import signup
from .views.users_view import get_users
from .views.otp_view import generate_otp, verify_otp

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('users/', get_users, name='get_users'),
    path('generate_otp/', generate_otp, name='generate_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
]
