import prompt


def welcome_user() -> str:
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name