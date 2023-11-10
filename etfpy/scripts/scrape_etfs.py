#!/bin/bash

import json
import os
from pathlib import Path

from etfpy.client._etfs_scraper import get_all_etfs
from etfpy.log import get_logger

ETFS_DATA_PATH = os.path.join(Path(__file__).parent.parent, "data", "etfs")

logger = get_logger(__name__)


def all_etfs_json(file_path: str = None) -> None:
    """Scrape all ETFs data from etfdb.com and save it to a json file to a location specified by file_path.

    Args:
        file_path (str, optional): Path to save the json file.
        If None, the json file will be saved to the project root directory.
    """
    # If file_path is None, set display_path to "project root folder"
    display_path = file_path

    if file_path is None:
        # Get the project root directory
        root_dir = Path(__file__).resolve().parents[1]
        file_path = os.path.join(root_dir, "etfs_list.json")
        display_path = "project root folder"

    page_size = 250
    logger.info("Scraping all ETFs data from etfdb.com")

    with open(file_path, "w") as f:
        json.dump(get_all_etfs(page_size), f)
    logger.debug("ETFs data saved to %s", display_path)


# TODO: Add argparser to specify params
if __name__ == "__main__":
    all_etfs_json()
