import string
from random import randint

from faker.generator import random


class Fake:
    @staticmethod
    def random_word(length=15):
        return " ".join(random.choice(string.ascii_letters) for _ in range(length))

    @staticmethod
    def random_short_word(length=8):
        return " ".join(random.choice(string.ascii_letters) for _ in range(length))

    @staticmethod
    def random_short_number(length=2):
        return " ".join(random.choice(randint(1, 100)) for _ in range(length))

    @staticmethod
    def base_str():
        return string.ascii_letters + str(string.digits)


