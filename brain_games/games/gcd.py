from math import gcd
from random import randint

MIN_VALUE = 1
MAX_VALUE = 100


def gcd_game() -> tuple[str, str]:
    number_1 = randint(MIN_VALUE, MAX_VALUE)
    number_2 = randint(MIN_VALUE, MAX_VALUE)
    question = f"{number_1} {number_2}"
    answer = str(gcd(number_1, number_2))
    return question, answer