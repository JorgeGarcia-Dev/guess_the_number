""" This is a function to validate integer type and range value """

def validate_difficulty_integer_range_decorator(method) -> callable:
    def wrapper(*args, **kwargs):
        while True:
            try:
                data: int = int(
                    input("Enter the level of difficulty: 1 = easy, 10 = hard: ")
                )
                if data >= 1 and data <= 10:
                    return method(data, *args, **kwargs)
                else:
                    print("The number must be between 1 and 10.")
            except ValueError:
                print("The character must be an integer.")

    return wrapper


@validate_difficulty_integer_range_decorator
def method_with_difficulty_validation(value) -> int:
    return value
