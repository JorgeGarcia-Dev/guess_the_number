import random

from utils.validate_integer_type import method_with_integer_validation

from utils.validate_difficulty_range import method_with_difficulty_validation


class GuessTheNumber:
    def __init__(self, difficulty) -> None:
        self.difficulty: int = difficulty
        self.selected_difficulty_level: int = difficulty * 10
        self.max_attempts: int = 5
        self.secret_number: int = random.randint(1, self.selected_difficulty_level)

    def play(self) -> None:
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
        print("Welcome to the game 'Guess the number'... Are you ready?\n")

    def print_instructions(self) -> None:
        print(
            f"You must find the secret number between 1 & {self.selected_difficulty_level}.\n"  # noqa
        )

    def get_player_number(self) -> int:
        player_number: int = method_with_integer_validation()
        return player_number

    def print_feedback(self, player_number: int, is_greater: bool) -> None:
        comparison = "greater" if is_greater else "less"
        print(f"The number is {comparison} than {player_number}.")

    def print_congratulations(self) -> None:
        print(
            f"Congratulations, you guessed the number! (The secret number was {self.secret_number})" # noqa
        )

    def print_loss_message(self) -> None:
        print(f"You lost! The secret number was {self.secret_number}.")


difficulty = method_with_difficulty_validation()
game = GuessTheNumber(difficulty)
game.play()
