from etfpy.utils import convert_spaces_to_underscore_and_lowercase


def convert_spaces_to_underscore_recursive_decorator(func):
    """A decorator that converts spaces to underscores in all keys in a nested dictionary returned by a function.

    Args:
        func: A function that returns a dict.

    Returns:
        A decorated function that returns a dict with all spaces in keys converted to underscores.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return convert_spaces_to_underscore_and_lowercase(result)

    return wrapper
