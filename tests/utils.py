import os.path
from pathlib import Path

import bs4

here = Path(__file__).parent


def soup(*args, **kwargs):
    with open(os.path.join(here, "data/jepy.html"), encoding="utf8") as f:
        data = bs4.BeautifulSoup(f, "html.parser")
    return data


def get_quotes(*args, **kwargs):
    with open(os.path.join(here, "data/test_quotes.txt"), encoding="utf8") as f:
        data = f.read()
    return data
