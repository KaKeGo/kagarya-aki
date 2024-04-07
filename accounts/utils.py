import re
import jwt

from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta



def validate_password_length(password):
    # ..Validator for user create password
    if len(password) < 4:
        return 'Password must be at least 4 characters'
    elif len(password) > 20:
        return 'Password its too long must be at least 20 characters'
    if not re.search('[a-z]', password):
        return 'Password must contain at least one lowercase letter'
    if not re.search("[A-Z]", password):
        return 'Password must contain at least one uppercase letter'
    if not re.search("[0-9]", password):
        return 'Password must contain at least one number'
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return 'Password must contain at least one special character' 
    return None

def validate__email(email):
    #..Validator for user create email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return 'Invalid email address'
    return None

def send_activation_email(user):
    #..Activation email to active account
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, settings.SECRET_KEY, algorithm='HS256')

    activation_link = f"{settings.SITE_DEV_URL}{reverse('accounts:activate_account', kwargs={'token': token})}"
    context = {'activation_link': activation_link}

    subject = 'KaGaRya - Account activation'
    html_message = render_to_string('email/activation_email.html', context)
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [user.email], html_message=html_message)
