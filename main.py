"""
Create a game "Guess the number" with Python.
"""

import random


def validate_number(message):
    while True:
        try:
            data = int(input("Enter " + message))
            return data
        except ValueError:
            print("The character must be an integer.")


def guess_the_number():
    print("Welcome to the game 'Guess the number'... Are you ready?\n")

    level_of_difficulty = validate_number(
        "the level of difficulty: 1 = easy, 10 = hard: "
    )

    selected_difficulty_level = int(f"{level_of_difficulty}0")

    print(
        "You must find the secret number "
        f"between 1 & {selected_difficulty_level}."
    )

    loop = 1

    secret_number = random.randint(1, selected_difficulty_level)

    while loop <= 5:
        player_number = validate_number("a number: ")

        if secret_number > player_number:
            loop += 1
            print(f"The number is greater than {player_number}.")

        elif secret_number < player_number:
            loop += 1
            print(f"The number is less than {player_number}.")

        else:
            print(
                "Congratulations,you guessed the number !!"
                f"(The secret number was {secret_number})"
            )
            break

    if loop > 5:
        print(f"You lost !! The secret number was {secret_number}.")


guess_the_number()
