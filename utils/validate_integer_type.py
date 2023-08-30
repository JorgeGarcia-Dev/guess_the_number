""" This is a function to validate integer type """

def validate_integer_type_decorator(method) -> callable:
    def wrapper(*args, **kwargs):
        while True:
            try:
                data: int = int(input("Guess a number: "))
                return method(data, *args, **kwargs)
            except ValueError:
                print("The character must be an integer.")
    return wrapper

@validate_integer_type_decorator
def method_with_integer_validation(value) -> int:
    return value