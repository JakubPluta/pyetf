import json


def dump_json(data, name):
    with open(name, 'w') as f:
        json.dump(data, f)
