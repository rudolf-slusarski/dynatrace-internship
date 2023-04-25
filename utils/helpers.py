from datetime import datetime
from re import match
import holidays


def validate_date(date):
    if not date:
        raise ValueError('date is required')

    if datetime.strptime(date, '%Y-%m-%d').weekday() >= 5:
        raise ValueError(f'given date ({date}) is not a weekday')

    if date in holidays.Poland():
        raise ValueError(
            f'given date ({date}) is a holiday: `{holidays.Poland().get(date)}')


def validate_currency(currency_code):
    if not currency_code:
        raise ValueError('currency code is required')

    if not match('^[aA-zZ]{3}$', currency_code):
        raise ValueError(
            'currency_code must be a valid three-letter currency code')


def validate_count(count):
    if not isinstance(count, int) or count < 1 or count > 255:
        raise ValueError('count must be a positive integer lower than 255')
