from random import choice, randint

MIN_VALUE = 0
MAX_VALUE = 100


def get_question_and_answer_calc() -> tuple[str, str]:
    number_1 = randint(MIN_VALUE, MAX_VALUE)
    number_2 = randint(MIN_VALUE, MAX_VALUE)
    available_operators = ['+', '-', '*']
    operator = choice(available_operators)
    question = f"{number_1} {operator} {number_2}"
    answer = str(eval(question))
    return question, answer