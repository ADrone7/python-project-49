from brain_games.cli import welcome_user
from brain_games.control import play_game
from brain_games.games.progression import progression_game


def main() -> None:
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print("What number is missing in the progression?")
    play_game(user_name, progression_game)


if __name__ == "__main__":
    main()