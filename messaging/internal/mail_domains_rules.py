import re

from messaging.internal.mail_domains import MailDomain


def remove_sentences_with_word_offer(content: str) -> str:
    """Removes sentences with word 'offer' from content."""
    pattern = r'[^.?!]*(?<=[.?\s!])offer(?=[\s.?!])[^.?!]*[.?!]'
    return re.sub(pattern, '', content).strip()


def extract_image_sources(content: str) -> str:
    """Extracts links from <img> and put them to content."""
    pattern = (
        r'<img src="((http(s?):)([\/|.|\w|\s|-])*\.(?:jpg|gif|png))"\s?\/>'
    )
    return re.sub(pattern, r'\1', content)


def replace_image_extension_gif_to_png(content: str) -> str:
    """Replace extension of images from .gif to .png."""
    pattern = r'(<img src=")((http(s?):)([\/|.|\w|\s|-])*\.)(gif)("\s?\/>)'
    return re.sub(pattern, r'\1\2png\7', content)


RULES_FOR_DOMAIN = {
    MailDomain.GMAIL_COM: (
        remove_sentences_with_word_offer,
    ),
    MailDomain.YANDEX_RU: (
        extract_image_sources,
    ),
    MailDomain.MAIL_RU: (
        replace_image_extension_gif_to_png,
    )
}
