import pytest

from messaging.internal import validators


@pytest.mark.parametrize('email', [
    'roxe@mail.ru',
    'testTeas123as@MaiL.ru',
    'x@long.domain.name.with.dots.ru'
])
def test_right_email_validation(email):
    """Tests validation of right email addresses."""
    assert validators.validate_email(email)


@pytest.mark.parametrize('email', [
    'roxemail.ru',
    'testTeas123as@MaiL',
    'long.domain.name.with.dots.ru'
])
def test_wrong_email_validation(email):
    """Tests validation of wrong email addresses."""
    assert not validators.validate_email(email)
