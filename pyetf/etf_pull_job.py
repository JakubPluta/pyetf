#!/usr/bin/env python

import json

import _clients


def get_etfs(client):
    etfs = client.scrape_etfs()
    if len(etfs) > 2500:
        with open('data.json', 'w') as f:
            json.dump(etfs, f)


if __name__ == '__main__':
    PAGE_LIMIT = 250
    client = _clients.ETFDBClient(page_size=PAGE_LIMIT)
    get_etfs(client)