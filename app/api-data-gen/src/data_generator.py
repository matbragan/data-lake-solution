from random import random, randint
from datetime import datetime, timedelta

from faker import Faker

from src.utils import fix_special_str, random_date, random_value

fake = Faker('pt_BR')


def transaction():
    """
    Generates a data transaction in dict format
    """
    today = datetime.now()
    data = {
        'id': int(random()*100000),
        'timestamp': random_date(today - timedelta(days=1), today),
        'product_id': randint(1, 21),
        'consumer_id': randint(1, 101),
        'paid_value': random_value(),
    }

    return data


def consumer():
    """
    Generates a consumer in dict format
    """
    data = {
        'id': randint(1, 101),
        'name': fix_special_str(fake.name()),
        'address': fix_special_str(fake.address().replace('\n', ' ')),
        'phone_number': fake.phone_number(),
        'birthday': fake.date_of_birth(minimum_age=18, maximum_age=80)
    }

    return data

def product():
    """
    Generates a product in dict format
    """
    data = {
        'id': randint(1, 21),
        'name': fix_special_str(fake.name()),
        'value': random_value()
    }
    return data
