import re


def validate_email(email: str) -> bool:
    """Validates email address."""
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_pattern, email))
