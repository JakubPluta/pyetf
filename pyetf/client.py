import time
import asyncio
import aiohttp
import requests
from requests import HTTPError


class BaseClient:
    BASE_URI = "https://etfdb.com"

    def __init__(self, number_of_pages = None, page_size: int = 500):
        self.api_url = 'https://etfdb.com/api/screener/'
        self.base_url = "https://etfdb.com"
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
                   'Accept': 'application/json'}

        self._post_json_data = {"tab": "returns", "page": 1, 'per_page' : page_size, "only": ["meta", "data", None]}

        try:
            self._meta = self.get_metadata()['meta']
        except (KeyError, HTTPError):
            self._meta = {}

        self.total_pages = self._meta.get('total_pages')
        if number_of_pages:
            self.total_pages = number_of_pages

        self.total_records = self._meta.get('total_records')
        self.page_size = page_size

        self._data = []

    def get_metadata(self):
        return requests.post(self.api_url, json=self._post_json_data, headers=self.headers).json()

    def parse_etf_record(self, obj: dict):
        try:
            return {
                'symbol': obj['symbol'].get('text'),
                'name': obj['name'].get('text'),
                'url': self.base_url + obj['symbol'].get('url'),
                'one_week_return': obj.get('one_week_return'),
                'one_year_return': obj.get('ytd'),
                'three_year_return': obj.get('three_ytd'),
                'five_year_return': obj.get('five_ytd'),
            }
        except KeyError as e:
            print(e)


class ETFDBClient(BaseClient):

    def scrape_etfs_from_single_page(self, page):
        self._post_json_data['page'] = page
        return requests.post(self.api_url, json=self._post_json_data, headers=self.headers).json()['data']

    def scrape_etfs(self):
        results = []
        for page in range(1, self.total_pages):
            etfs = self.scrape_etfs_from_single_page(page)
            results += self.prepare_list_of_etfs(etfs)
        return results

    def prepare_list_of_etfs(self, etfs):
        return [self.parse_etf_record(etf) for etf in etfs]


class AsyncETFDBClient(BaseClient):
    """Async client for etfdb.com"""

    BASE_URI = "https://etfdb.com"

    def __init__(self, number_of_pages = None, page_size: int = 25):
        super().__init__(number_of_pages,page_size)
        self.api_url = 'https://etfdb.com/api/screener/'
        self.base_url = "https://etfdb.com"
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
                   'Accept': 'application/json'}

        self._post_json_data = {"tab": "returns", "page": 1, 'per_page' : page_size, "only": ["meta", "data", None]}

        try:
            self._meta = self.get_metadata()['meta']
        except (KeyError, HTTPError):
            self._meta = {}

        self.total_pages = self._meta.get('total_pages')
        if number_of_pages:
            self.total_pages = number_of_pages

        self.total_records = self._meta.get('total_records')
        self.page_size = page_size

    def run(self):
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self.scrape_etfs())
        loop.run_until_complete(asyncio.sleep(1))
        loop.close()
        return data

    async def scrape_etfs_from_single_page(self, session, page):
        try:
            self._post_json_data['page'] = page
            time.sleep(1)
            async with session.post(self.api_url, json=self._post_json_data, headers=self.headers) as response:
                data = await response.json()
                results = await self.prepare_list_of_etfs(data['data'])
                return results
        except requests.exceptions.ConnectionError as e:
            print(e)

    async def prepare_list_of_etfs(self, etfs):
        return [await self.parse_etf_record(etf) for etf in etfs]

    async def parse_etf_record(self, obj: dict):
        try:
            return {
                'symbol': obj['symbol'].get('text'),
                'name': obj['name'].get('text'),
                'url': self.base_url + obj['symbol'].get('url'),
                'one_week_return': obj.get('one_week_return'),
                'one_year_return': obj.get('ytd'),
                'three_year_return': obj.get('three_ytd'),
                'five_year_return': obj.get('five_ytd'),
            }
        except KeyError as e:
            print(e)

    async def scrape_etfs(self):
        tasks = []
        data = []
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            for page in range(1, self.total_pages):
                tasks.append(self.scrape_etfs_from_single_page(session, page))

            for result in await asyncio.gather(*tasks):
                data += result
            return data
