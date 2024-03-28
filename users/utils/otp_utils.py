import random

def generate_otp_code(length=6):
    """Generate a random numeric string of specified length."""
    otp_code = ''.join(random.choices('0123456789', k=length))
    return otp_code