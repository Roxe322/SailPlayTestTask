from __future__ import annotations

import enum


class MailDomain(enum.Enum):
    """Available mail domains."""
    MAIL_RU = 1
    GMAIL_COM = 2
    YANDEX_RU = 3

    @classmethod
    def parse_domain(cls, domain: str) -> MailDomain:
        """
        Gets domain and returns associated enum element for it,
        for unknown domain uses MailDomain.GMAIL_COM.
        """
        pattern = {
            'mail.ru': MailDomain.MAIL_RU,
            'gmail.com': MailDomain.GMAIL_COM,
            'yandex.ru': MailDomain.YANDEX_RU,
        }

        return pattern.get(domain, MailDomain.GMAIL_COM)
