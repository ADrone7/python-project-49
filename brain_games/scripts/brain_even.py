from brain_games.cli import welcome_user
from brain_games.control import play_game
from brain_games.games.even import get_question_and_answer_even


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_game(user_name, get_question_and_answer_even)


if __name__ == "__main__":
    main()