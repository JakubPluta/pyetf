#!/bin/bash

import json
import os
from pathlib import Path

from etfpy.client._etfs_scraper import get_all_etfs
from etfpy.log import get_logger

ETFS_DATA_PATH = os.path.join(Path(__file__).parent.parent, "data", "etfs")

logger = get_logger(__name__)

# TODO: Add argparser to specify params
if __name__ == "__main__":
    page_size = 250
    file_path = os.path.join(ETFS_DATA_PATH, "etfs_list.json")
    with open(file_path, "w") as f:
        json.dump(get_all_etfs(page_size), f)
    logger.debug("data was stored in %s", file_path)
