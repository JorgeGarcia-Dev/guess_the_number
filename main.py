""" This is a docstring for the `GuessTheNumber`. """

import random

from utils.validate_integer_type import method_with_integer_validation

from utils.validate_difficulty_range import method_with_difficulty_validation


class GuessTheNumber:
    """
    The `GuessTheNumber` class allows players to guess a secret number within a
    specified range and provides feedback on their guesses.

    :param difficulty: The `difficulty` parameter is an integer that represents the
        level of difficulty for the game.

    :type difficulty:
        int

    :return:
        None
    """

    def __init__(self, difficulty) -> None:
        """
        The function initializes the attributes of a class instance related to
        a game difficulty level.

        :param difficulty: The `difficulty` parameter is an integer that represents the
        level of difficulty for the game.
        """

        self.difficulty: int = difficulty
        self.selected_difficulty_level: int = difficulty * 10
        self.max_attempts: int = 5
        self.secret_number: int = random.randint(1, self.selected_difficulty_level)

    def play(self) -> None:
        """
        The function `play` allows the player to guess a secret number and provides
        feedback on whether the guess is greater or smaller than the secret number.

        :params:
            None

        :return:
            None
        """
        self.print_welcome_message()
        self.print_instructions()

        attempts: int = 1

        while attempts <= self.max_attempts:
            player_number: int = self.get_player_number()

            if self.secret_number > player_number:
                attempts += 1
                self.print_feedback(player_number, is_greater=True)

            elif self.secret_number < player_number:
                attempts += 1
                self.print_feedback(player_number, is_greater=False)

            else:
                self.print_congratulations()
                break

        if attempts > self.max_attempts:
            self.print_loss_message()

    def print_welcome_message(self) -> None:
        """
        The function `print_welcome_message` prints a welcome message for the game
        "Guess the number".
        """
        print("Welcome to the game 'Guess the number'... Are you ready?\n")

    def print_instructions(self) -> None:
        """
        The function `print_instructions` prints a message that instructs the user to
        find a secret number within a specified range.
        """
        print(
            f"You must find the secret number between 1 & {self.selected_difficulty_level}.\n"  # noqa
        )

    def get_player_number(self) -> int:
        """
        The function "get_player_number" returns an integer representing the player
        number after validating it using a method.

        :return:
            The player number, which is an integer.
        """
        player_number: int = method_with_integer_validation()
        return player_number

    def print_feedback(self, player_number: int, is_greater: bool) -> None:
        """
        The function prints feedback indicating whether a given number is greater or
        less than a player number.

        :param player_number:
            An integer representing the player's number.

        :type player_number:
            int

        :param is_greater:
            A boolean value indicating whether the number is greater than the player.

        number
        :type is_greater:
            bool
        """
        comparison = "greater" if is_greater else "less"
        print(f"The number is {comparison} than {player_number}.")

    def print_congratulations(self) -> None:
        """
        The function `print_congratulations` prints a congratulatory message with the
        secret number.
        """
        print(
            f"Congratulations, you guessed the number! (The secret number was {self.secret_number})"  # noqa
        )

    def print_loss_message(self) -> None:
        """
        The function prints a loss message with the secret number.
        """
        print(f"You lost! The secret number was {self.secret_number}.")


difficulty = method_with_difficulty_validation()
game = GuessTheNumber(difficulty)
game.play()
