import pytest

from messaging.internal.mail_domains import MailDomain


@pytest.mark.parametrize('domain, enum_elem', [
    ('mail.ru', MailDomain.MAIL_RU),
    ('gmail.com', MailDomain.GMAIL_COM),
    ('yandex.ru', MailDomain.YANDEX_RU),
    ('unknown.com', MailDomain.GMAIL_COM),
])
def test_domain_parsing(domain, enum_elem):
    """Tests right parsing of domain."""
    assert MailDomain.parse_domain(domain) == enum_elem
