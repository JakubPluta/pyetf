import os.path
from pathlib import Path

import bs4

here = Path(__file__).parent


def soup(*args, **kwargs):
    with open(os.path.join(here, "jepy.html"), encoding="utf8") as f:
        data = bs4.BeautifulSoup(f, "html.parser")
    return data
