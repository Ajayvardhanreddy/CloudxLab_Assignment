from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def is_email_valid(email: str) -> bool:
    """
        is_email_valid(email) is a function which takes email as an parameter and checks whether the email is valid or not.
    """
    try:
        validate_email(email)
    except ValidationError as e:
        print(e)
        return False
    else:
        return True
