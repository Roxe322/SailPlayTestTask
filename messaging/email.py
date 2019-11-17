from messaging.internal.mail_domains import MailDomain
from messaging.internal.mail_domains_rules import RULES_FOR_DOMAIN
from messaging.internal.validators import validate_email


class Email:
    """Implements interface for sending emails."""
    def __init__(self, email: str, content: str) -> None:
        if not validate_email(email):
            raise ValueError('Invalid email address')

        _, domain = email.lower().split('@')
        parsed_domain = MailDomain.parse_domain(domain)

        self.email = email
        self.content = self._prepare_content(parsed_domain, content)

    def _prepare_content(self, domain: MailDomain, content: str) -> str:
        """
        Prepares content depending on rules of domain.
        """
        rules = RULES_FOR_DOMAIN[domain]
        for rule in rules:
            content = rule(content)

        return content

    def send(self):
        """
        Returns filtered self.content and self.email where content
        should be send.
        """
        return {'email': self.email,
                'content': self.content}
