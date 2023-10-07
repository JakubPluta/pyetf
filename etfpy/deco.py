import functools

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


def lowercase_and_underscore_column_names(func):
    """A decorator that lowercases and underscores all column names in a DataFrame.

    Args:
        func: The function to decorate.

    Returns:
        A decorated function that lowercases and underscores all column names in a DataFrame.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        df = func(*args, **kwargs)
        df.columns = [col.lower().replace(" ", "_") for col in df.columns]
        return df

    return wrapper
