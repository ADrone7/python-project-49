from brain_games.cli import welcome_user
from brain_games.control import play_game
from brain_games.games.prime import get_question_and_answer_prime


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    play_game(user_name, get_question_and_answer_prime)


if __name__ == "__main__":
    main()