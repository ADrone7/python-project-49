from random import randint

MIN_LEN = 5
MAX_LEN = 10
MIN_STEP = 1
MAX_STEP = 15
MIN_START = 0
MAX_START = 20


def progression_game() -> tuple[str, str]:
    progression_length = randint(MIN_LEN, MAX_LEN)
    progression_step = randint(MIN_STEP, MAX_STEP)
    progression_start = randint(MIN_START, MAX_START)
    progression = [str(progression_start + i * progression_step)
                   for i in range(progression_length)]
    hidden_element_index = randint(0, progression_length - 1)
    answer = progression[hidden_element_index]
    progression[hidden_element_index] = ".."
    question = ' '.join(progression)
    return question, answer