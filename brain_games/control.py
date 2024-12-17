from typing import Callable

import prompt


def play_game(user_name: str,
              game: Callable[[], tuple[str, str]],
              rounds: int = 3) -> None:
    for i in range(rounds):
        question, right_answer = game()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == right_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. " +
                   f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")