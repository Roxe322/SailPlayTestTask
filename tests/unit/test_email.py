import pytest

from messaging.email import Email


def test_email_raises_value_error_on_wrong_email():
    """Tests raising ValueError with invalid email on initializing Email."""
    with pytest.raises(ValueError, match="Invalid email address"):
        Email('wrongemail', 'some_content')


def test_email_not_raises_value_error_on_right_email():
    """Tests that with valid address no error was raised."""
    address = 'nice_email@yandex.ru'
    email = Email(address, 'some_content')
    assert email.email == address


@pytest.mark.parametrize('address, content, filtered_content', [
    ('test1@gmail.com',
     'Hello gmail! I have an offer for you.',
     'Hello gmail!'),
    ('test2@yandex.ru',
     'Hello yandex! I have an pic <img src="https://spam.org/pic1.png" /> '
     'for you.',
     'Hello yandex! I have an pic https://spam.org/pic1.png for you.'),
    ('test3@mail.ru',
     'Hello mail! I have an pic <img src="https://spam.org/pic1.gif" /> '
     'for you.',
     'Hello mail! I have an pic <img src="https://spam.org/pic1.png" /> '
     'for you.'),
    ('test4@sailplay.ru',
     'Hello another mail client! I have an offer for you.',
     'Hello another mail client!')

])
def test_sending(address, content, filtered_content):
    email = Email(address, content)
    result = email.send()

    assert result['content'] == filtered_content
