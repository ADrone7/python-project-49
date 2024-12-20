from itertools import accumulate, cycle
from math import log
from random import uniform

SMALL_PRIMES = (2, 3)
FIRST_POSSIBLE_DIVISOR = 5
LEFT_RANGE = 1e-6
RIGHT_RANGE = 1
MAX_VALUE = 1000
LOG_BASE = 10


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    
    for prime in SMALL_PRIMES:
        if num % prime == 0 and num != prime:
            return False
    
    divisors = accumulate(cycle([2, 4]), initial=FIRST_POSSIBLE_DIVISOR)
    max_divisor_to_check = int(num**(0.5)) + 1
    for possible_divisor in divisors:
        if possible_divisor > max_divisor_to_check:
            break
        if num % possible_divisor == 0:
            return False
        
    return True


def get_question_and_answer_prime() -> tuple[str, str]:
    number = int(MAX_VALUE / log(LEFT_RANGE, LOG_BASE) *
                 log(uniform(LEFT_RANGE, RIGHT_RANGE), LOG_BASE))
    question = str(number)
    answer = "yes" if is_prime(number) else "no"
    return question, answer