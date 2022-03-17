from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def uri_validator(value):
    try:
        result = urlparse(value)
        if not all([result.scheme, result.netloc]) :
            raise ValidationError('Invalid input')  
    except:
        raise ValidationError('Invalid input')   