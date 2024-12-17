from brain_games.cli import welcome_user
from brain_games.control import play_game
from brain_games.games.calc import calc_game


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print("What is the result of the expression?")
    play_game(user_name, calc_game)


if __name__ == "__main__":
    main()