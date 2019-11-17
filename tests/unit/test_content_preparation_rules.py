import pytest

from messaging.internal import mail_domains_rules


@pytest.mark.parametrize('content, result', [
    ('Hello! I have offer.', 'Hello!'),
    ('Here is your offer.', ''),
    ('Is it offer? Yes', 'Yes'),
    ('I have offer! You have offer? No!', 'No!'),
])
def test_remove_sentence_with_offer_word_rule(content, result):
    """Tests right sentence with word 'offer' removing."""
    assert result == mail_domains_rules.remove_sentences_with_word_offer(
        content
    )


@pytest.mark.parametrize('content, result', [
    ('Hello! I have offer.', 'Hello!'),
    ('Here is your offer.', ''),
    ('Is it offer? Yes', 'Yes'),
    ('I have offer! You have offer? No!', 'No!'),
])
def test_remove_sentence_with_offer_word_rule(content, result):
    """Tests right sentence with word 'offer' removing."""
    assert result == mail_domains_rules.remove_sentences_with_word_offer(
        content
    )


@pytest.mark.parametrize('content, result', [
    ('Hello, check this image <img src="https://spam.org/pic1.png"/>',
     'Hello, check this image https://spam.org/pic1.png'),
    ('<img src="https://spam.org/pic1.png"/>', 'https://spam.org/pic1.png'),
    ('No image here', 'No image here'),
    ('Multiple images <img src="https://spam.org/pic1.png"/> <img src="https://spam.org/pic2.png"/>',
     'Multiple images https://spam.org/pic1.png https://spam.org/pic2.png')
])
def test_extracting_images_from_img_tag(content, result):
    """Tests extracting images sources from <img> tag."""
    assert result == mail_domains_rules.extract_image_sources(content)


@pytest.mark.parametrize('content, result', [
    ('Hello, check this image <img src="https://spam.org/pic1.gif"/>',
     'Hello, check this image <img src="https://spam.org/pic1.png"/>'),
    ('<img src="https://spam.org/pic1.gif"/>',
     '<img src="https://spam.org/pic1.png"/>'),
    ('No image here', 'No image here'),
    ('Hello, check this image <img src="https://spam.org/pic1.png"/>',
     'Hello, check this image <img src="https://spam.org/pic1.png"/>'),
    ('Multiple images: <img src="https://spam.org/pic1.gif"/> '
     '<img src="https://spam.org/pic2.gif"/>',
     'Multiple images: <img src="https://spam.org/pic1.png"/> '
     '<img src="https://spam.org/pic2.png"/>')
])
def test_replacing_image_extension_from_gif_to_png(content, result):
    """Tests replacing image extension from gif to png."""
    assert result == mail_domains_rules.replace_image_extension_gif_to_png(
        content
    )
