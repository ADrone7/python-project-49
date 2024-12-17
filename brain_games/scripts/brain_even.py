from brain_games.cli import welcome_user
from brain_games.control import play_game
from brain_games.games.even import even_game


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_game(user_name, even_game)


if __name__ == "__main__":
    main()