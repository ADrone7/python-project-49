from itertools import accumulate, cycle
from math import log
from random import uniform

SMALL_PRIMES = set([2, 3])
LEFT_RANGE = 1e-6
RIGHT_RANGE = 1
MAX_VALUE = 1000
LOG_BASE = 10


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    
    for prime in SMALL_PRIMES:
        if num % prime == 0 and num != prime:
            return False
    
    for possible_divisor in accumulate(cycle([2, 4]), initial=5):
        if possible_divisor > int(num**(0.5) + 1):
            break
        if num % possible_divisor == 0:
            return False
        
    return True


def prime_game() -> tuple[str, str]:
    number = int(MAX_VALUE / log(LEFT_RANGE, LOG_BASE) *
                 log(uniform(LEFT_RANGE, RIGHT_RANGE), LOG_BASE))
    question = str(number)
    answer = "yes" if is_prime(number) else "no"
    return question, answer