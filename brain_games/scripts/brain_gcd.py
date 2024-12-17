from brain_games.cli import welcome_user
from brain_games.control import play_game
from brain_games.games.gcd import gcd_game


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    play_game(user_name, gcd_game)


if __name__ == "__main__":
    main()