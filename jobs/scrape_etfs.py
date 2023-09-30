#!/bin/bash

import json
import os
from pathlib import Path

from pyetf.etf_scraper import get_all_etfs

ETFS_DATA_PATH = os.path.join(Path(__file__).parent.parent, "data", "etfs")


if __name__ == '__main__':
    page_size = 250
    file_path = os.path.join(ETFS_DATA_PATH, "etfs_list.json")
    with open(file_path, 'w') as f:
        json.dump(get_all_etfs(page_size), f)