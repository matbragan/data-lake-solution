from random import randrange, uniform, randint
from datetime import timedelta
import unicodedata


def fix_special_str(string):
    """
    Remove special characters
    """
    normalized_text = unicodedata.normalize('NFKD', string)
    return normalized_text.encode('ASCII', 'ignore').decode('utf-8')


def random_date(start, end):
    """
    Return a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_value():
    """
    Return a random value between 40 and 220.
    """
    return round(uniform(0.5, 1) * randint(80, 220), 2)
