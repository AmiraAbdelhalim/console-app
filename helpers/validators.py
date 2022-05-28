import re

def validate_email(email):
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.match(email_regex, email):
        return True
    return None


def validate_mobile(mobile):
    mobile_regex = '^01[0125][0-9]{8}$'
    if re.match(mobile_regex, mobile):
        return True
    return None


def confirm_user_password(password, confirm_password):
    if password == confirm_password:
        return True
    return None
