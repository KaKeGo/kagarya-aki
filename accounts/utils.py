import re

def validate_password_length(password):
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
