from django.core.validators import RegexValidator


MOBILE_REGEX = r'^01[013456789][\d]{8}$'
MOBILE_VALIDATOR = RegexValidator(MOBILE_REGEX, "Invalid mobile number.")