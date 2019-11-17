# Test task for SailPlay
https://github.com/iamthegoodbot/sailplay-test/blob/master/backend/README.md
# Usage
```python
from messaging.email import Email
email = Email('test1@gmail.com', 'Hello gmail! I have an offer for you.')
email.send()
>>> {'email': "test1@gmail.com", 'content': 'Hello gmail!'}
```
# Testing
* Install test requirements using ```pip install -r requirements-test.txt```.
* run ```python -m pytest --cov=messaging --cov-report=html``` for unit tests and coverage report.
* run ```python -m mypy messaging ``` for static type checking.
* run ```python -m isort -rc messaging --check-only``` for check imports order.
