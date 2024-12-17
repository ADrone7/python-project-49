from random import randint

MIN_VALUE = 0
MAX_VALUE = 1000


def even_game() -> tuple[str, str]:
    number = randint(MIN_VALUE, MAX_VALUE)
    question = str(number)
    answer = "yes" if number % 2 == 0 else "no"
    return question, answer