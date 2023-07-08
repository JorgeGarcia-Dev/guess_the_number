"""
Create a game "Guess the number" with Python.
"""

import random


def validate_difficulty_integer_range(message):
    """
    This function validates the type and range of numbers.

    Parameters:
    message (str): The message to display to the user.

    Returns:
    int: The validated number.

    Examples:
    >>> validate_difficulty_integer_range(
        "Enter the level of difficulty: 1 = easy, 10 = hard: "
        )
    Enter the level of difficulty: 1 = easy, 10 = hard: 10
    10

    >>> validate_difficulty_integer_range(
        "Enter the level of difficulty: 1 = easy, 10 = hard: "
        )
    Enter the level of difficulty: 1 = easy, 10 = hard: 5
    5

    >>> validate_difficulty_integer_range(
        "Enter the level of difficulty: 1 = easy, 10 = hard: "
        )
    Enter the level of difficulty: 1 = easy, 10 = hard: "10"
    ValueError: invalid literal for int() with base 10: '10'

    >>> validate_difficulty_integer_range(
        "Enter the level of difficulty: 1 = easy, 10 = hard: "
        )
    Enter the level of difficulty: 1 = easy, 10 = hard: diez
    ValueError: invalid literal for int() with base 10: 'diez'

    >>> validate_difficulty_integer_range(
        "Enter the level of difficulty: 1 = easy, 10 = hard: "
        )
    Enter the level of difficulty: 1 = easy, 10 = hard: 20
    The number must be between 1 and 10.
    """
    while True:
        try:
            data = int(input("Enter " + message))
            if data >= 1 and data <= 10:
                return data
            else:
                print("The number must be between 1 and 10.")
        except ValueError:
            print("The character must be an integer.")

        except TypeError as error:
            print(error)


def validate_integer_type(message):
    """
    This function validates the type and range of numbers.

    Parameters:
    message (str): The message to display to the user.

    Returns:
    int: The validated number.

    Examples:
    >>> validate_typ__number(
        "Enter a number: "
        )
    Enter a number: 10
    10

    >>> validate_integer_type(
        "Enter a number: "
        )
    Enter a number: 5
    5

    >>> validate_integer_type(
        "Enter a number: "
        )
    Enter a number: "10"
    ValueError: invalid literal for int() with base 10: '10'

    >>> validate_integer_type(
        "Enter a number: "
        )
    Enter a number: diez
    ValueError: invalid literal for int() with base 10: 'diez'
    """
    while True:
        try:
            data = int(input("Enter " + message))
            return data
        except ValueError:
            print("The character must be an integer.")

        except TypeError as error:
            print(error)


def guess_the_number():
    """
    This function implements the 'Guess the Number' game.

    The game prompts the user to guess a secret number within
    a given range of difficulty levels.
    The user has 5 attempts to guess the number. After each guess,
    the game provides feedback on whether the secret number is greater
    or less than the guess.
    If the user guesses the number correctly within the allowed attempts,
    they win the game. Otherwise, they lose.

    Parameters:
    message (str): The message to display to the user.

    Returns:
    message (str): Response message depending
    on whether the number is higher or lower,
    if the user has guessed the number,
    or if his chances have been exhausted.

    Example:
    >>> guess_the_number()
    Welcome to the game 'Guess the number'... Are you ready?

    Enter the level of difficulty: 1 = easy, 10 = hard: 5
    You must find the secret number between 1 & 50.
    Guess a number: 25
    The number is greater than 25.
    Guess a number: 40
    The number is less than 40.
    Guess a number: 35
    Congratulations, you guessed the number! (The secret number was 35)
    """
    print("Welcome to the game 'Guess the number'... Are you ready?\n")

    level_of_difficulty = validate_difficulty_integer_range(
        "the level of difficulty: 1 = easy, 10 = hard: "
    )

    selected_difficulty_level = int(f"{level_of_difficulty}0")

    print(
        "You must find the secret number "
        f"between 1 & {selected_difficulty_level}."
    )

    attempts = 1
    max_attempts = 5

    secret_number = random.randint(1, selected_difficulty_level)

    while attempts <= max_attempts:
        player_number = validate_integer_type("a number: ")

        if secret_number > player_number:
            attempts += 1
            print(f"The number is greater than {player_number}.")

        elif secret_number < player_number:
            attempts += 1
            print(f"The number is less than {player_number}.")

        else:
            print(
                "Congratulations,you guessed the number !!"
                f"(The secret number was {secret_number})"
            )
            break

    if attempts > 5:
        print(f"You lost !! The secret number was {secret_number}.")


guess_the_number()
