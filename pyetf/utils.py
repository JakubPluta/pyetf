import json
import functools


def dump_json(data, name):
    with open(name, "w") as f:
        json.dump(data, f)


def _try(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)

    return inner
