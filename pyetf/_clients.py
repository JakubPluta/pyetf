import time
import asyncio
import aiohttp
from requests import HTTPError
import functools
import json
import os

import bs4
import requests

from pyetf.utils import _try, retry_session, dump_json


class InvalidETFException(Exception):
    """Invalid ETF Exception class"""


class BaseClient:
    BASE_URI = "https://etfdb.com"

    def __init__(self, number_of_pages=None, page_size: int = 500):
        self.session = retry_session()
        self.api_url = "https://etfdb.com/api/screener/"
        self.base_url = "https://etfdb.com"
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
                "Accept": "application/json",
            }
        )

        self._post_json_data = {
            "tab": "returns",
            "page": 1,
            "per_page": page_size,
            "only": ["meta", "data", None],
        }

        try:
            self._meta = self.get_metadata()["meta"]
        except (KeyError, HTTPError):
            self._meta = {}

        self.total_pages = self._meta.get("total_pages")
        if number_of_pages:
            self.total_pages = number_of_pages

        self.total_records = self._meta.get("total_records")
        self.page_size = page_size

        self._data = []

    def get_metadata(self):
        return self.session.post(
            self.api_url, json=self._post_json_data, timeout=10
        ).json()

    def parse_etf_record(self, obj: dict):
        try:
            return {
                "symbol": obj["symbol"].get("text"),
                "name": obj["name"].get("text"),
                "url": self.base_url + obj["symbol"].get("url"),
                "one_week_return": obj.get("one_week_return"),
                "one_year_return": obj.get("ytd"),
                "three_year_return": obj.get("three_ytd"),
                "five_year_return": obj.get("five_ytd"),
            }
        except KeyError as e:
            print(e)


class ETFDBClient(BaseClient):
    def scrape_etfs_from_single_page(self, page):
        time.sleep(5)
        self._post_json_data["page"] = page
        print("Getting page ", page)

        try:
            data = self.session.post(
                self.api_url, json=self._post_json_data, timeout=15
            ).json()["data"]
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            data = self.session.post(
                self.api_url, json=self._post_json_data, timeout=15
            ).json()["data"]

        return data

    def scrape_etfs(self):
        results = []
        for page in range(1, self.total_pages + 1):
            etfs = self.scrape_etfs_from_single_page(page)
            print("Number of etfs ", len(etfs))
            results += self.prepare_list_of_etfs(etfs)
        return results

    def prepare_list_of_etfs(self, etfs):
        return [self.parse_etf_record(etf) for etf in etfs]


# TODO: Work on retry policy with aiohttp.ClientSession
class AsyncETFDBClient(BaseClient):
    """Async client for etfdb.com"""

    BASE_URI = "https://etfdb.com"

    def __init__(self, number_of_pages=None, page_size: int = 25):
        super().__init__(number_of_pages, page_size)
        self.api_url = "https://etfdb.com/api/screener/"
        self.base_url = "https://etfdb.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "application/json",
        }

        self._post_json_data = {
            "tab": "returns",
            "page": 1,
            "per_page": page_size,
            "only": ["meta", "data", None],
        }

        try:
            self._meta = self.get_metadata()["meta"]
        except (KeyError, HTTPError):
            self._meta = {}

        self.total_pages = self._meta.get("total_pages")
        if number_of_pages:
            self.total_pages = number_of_pages

        self.total_records = self._meta.get("total_records")
        self.page_size = page_size

    def run(self):
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self.scrape_etfs())
        loop.run_until_complete(asyncio.sleep(1))
        loop.close()
        return data

    async def scrape_etfs_from_single_page(self, session, page):
        try:
            self._post_json_data["page"] = page
            time.sleep(1)
            async with session.post(
                self.api_url, json=self._post_json_data, headers=self.headers
            ) as response:
                data = await response.json()
                results = await self.prepare_list_of_etfs(data["data"])
                return results
        except requests.exceptions.ConnectionError as e:
            print(e)

    async def prepare_list_of_etfs(self, etfs):
        return [await self.parse_etf_record(etf) for etf in etfs]

    async def parse_etf_record(self, obj: dict):
        try:
            return {
                "symbol": obj["symbol"].get("text"),
                "name": obj["name"].get("text"),
                "url": self.base_url + obj["symbol"].get("url"),
                "one_week_return": obj.get("one_week_return"),
                "one_year_return": obj.get("ytd"),
                "three_year_return": obj.get("three_ytd"),
                "five_year_return": obj.get("five_ytd"),
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


def load_ticker_list() -> list:
    """Loads all available tickers from etfdb.com

    Returns
    -------
    list of available etf tickers
    """

    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "etfdb.json"
    )
    with open(path, "r") as f:
        data = json.load(f)
    return data


tickers: dict = {etf.get("symbol"): etf for etf in load_ticker_list()}


class ETFDBScraper:
    """etfdb scraper client"""

    BASE_URL = "https://etfdb.com"

    def __init__(self, ticker: str):
        self.session = retry_session()
        if ticker.upper() in tickers:
            self.ticker = ticker.upper()
            self._ticker_scraped_data = tickers.get(self.ticker)

            self.ticker_data = {
                "name": self._ticker_scraped_data.get("name"),
                "symbol": self._ticker_scraped_data.get("symbol"),
                "url": self._ticker_scraped_data.get("url"),
            }
        else:
            raise InvalidETFException(f"{ticker} doesn't exist in ETF Database\n")

        try:
            self.__soup = self._make_soup_request()
        except Exception as e:
            raise HTTPError(f"Couldn't load data for {self.ticker}") from e

    def _prepare_url(self,) -> str:
        """Builds url for given ticker."""

        return f"{self.BASE_URL}/etf/{self.ticker}/"

    @functools.lru_cache(maxsize=128)
    def _make_soup_request(self) -> bs4.BeautifulSoup:
        """Make GET request to etfdb.com, and put response into BeautifulSoup data structure.

        Returns
        -------
        BeautifulSoup object ready to parse with bs4 library
        """

        url = self._prepare_url()
        response = self.session.get(url)
        return bs4.BeautifulSoup(response.text, "html.parser")

    @_try
    def _get_profile_container(self) -> dict:
        """Parse profile-container div into dictionary with base statistics."""

        profile_container = [
            x.find_all("span")
            for x in self.__soup .find("div", {"class": "profile-container"}).find_all(
                "div", class_="row"
            )
        ]
        results = []
        for spans in profile_container:
            record = tuple(span.text.strip() for span in spans)
            if len(record) > 2:
                record = record[:2]
            if len(record) != 2:
                continue
            results.append(record)
        return {x: y for x, y in results}

    @_try
    def _trading_data(self) -> dict:
        """Get trading data"""
        trading_data = self.__soup .find(
            "div", {"class": "data-trading bar-charts-table"}
        ).find_all("li")
        trading_dict = {
            li.select_one(":nth-child(1)")
            .text.strip(): li.select_one(":nth-child(2)")
            .text.strip()
            for li in trading_data
        }
        return {k: v for k, v in trading_dict.items() if v != ""}

    @_try
    def _asset_categories(self) -> dict:
        """Get asset categories data"""

        theme = self.__soup .find("div", {"id": "etf-ticker-body"}).find_all(
            "div", class_="ticker-assets"
        )
        if not theme or len(theme) < 1:
            raise Exception("Asset categories not found\n")

        theme = theme[1]
        theme_dict = {
            row.select_one(":nth-child(1)")
            .text.strip(): row.select_one(":nth-child(2)")
            .text.strip()
            for row in theme.find_all("div", class_="row")
        }
        return theme_dict

    @_try
    def _factset_classification(self) -> dict:
        """Get factset information"""

        factset = self.__soup .find("div", {"id": "factset-classification"}).find_all("li")
        factset_dict = {
            li.select_one(":nth-child(1)")
            .text.strip(): li.select_one(":nth-child(2)")
            .text.strip()
            for li in factset
        }
        return factset_dict

    @_try
    def _number_of_holdings(self) -> dict:
        """Get number of holdings for given etf"""

        holdings_table = self.__soup .find("table", {"id": "holdings-table"}).find("tbody")
        table_rows = [x.text.strip() for x in holdings_table.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    @_try
    def _size_locations(self) -> dict:
        """Get size allocations of holdings for given etf"""

        size_locations = self.__soup .find("table", {"id": "size-table"}).find("tbody")
        table_rows = [x.text.strip() for x in size_locations.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    @_try
    def _valuation(self) -> dict:
        """Get ETF valuation metrics."""
        valuation = (
            self.__soup .find("div", {"id": "etf-ticker-valuation-dividend"})
            .find("div", {"id": "valuation"})
            .find_all("div", class_="row")
        )
        values = [
            div.text for div in valuation[1].find_all("div", class_="text-center")
        ]
        return {values[0]: values[1]}

    @_try
    def _basic_info(self):
        """
        Return basic information about ETF. Like:
            - Issuer, Brand, Expense Ration, Home Page, Inception, Index

        Returns
        -------
        dict:
            ETF basic information
        """

        etf_ticker_body = self.__soup .find("div", {"id": "etf-ticker-body"}).find(
            "div", class_="row"
        )
        basic_information = {}

        for row in etf_ticker_body.find_all("div", class_="row"):
            key = row.select_one(":nth-child(1)").text.strip()
            value = row.select_one(":nth-child(2)")
            try:
                href = value.find("a")["href"]
                if href and key != "ETF Home Page":
                    value_text = self.BASE_URL + href
                else:
                    value_text = href
            except (KeyError, TypeError):
                value_text = value.text.strip()

            if key == "ETF Home Page" and value_text.startswith(self.BASE_URL):
                value_text.replace(self.BASE_URL, "")

            basic_information.update({key: value_text})

        basic_information.update(self._get_profile_container())
        basic_information.update(self._valuation())
        basic_information.update(self._trading_data())
        basic_information.update(self._asset_categories())
        basic_information.update(self._factset_classification())
        if "Analyst Report" in basic_information:
            basic_information.pop("Analyst Report")
        return basic_information

    @_try
    def _dividends(self) -> dict:
        """Get ETF dividend information."""

        results = {}
        dividend = (
            self.__soup .find("div", {"id": "etf-ticker-valuation-dividend"})
            .find("div", {"id": "dividend"})
            .find("tbody")
        )
        rows = [x.find_all("td") for x in dividend.find_all("tr")]
        category = None
        for row in rows:
            for idx, td in enumerate(row):
                data_th = td.get("data-th")
                text = td.text.strip()
                if idx == 0:
                    category = text
                    continue
                else:
                    if category not in results:
                        results[category] = {}

                    if data_th != "Fund":
                        continue
                    results[category] = text
        return results

    @_try
    def _holdings(self) -> dict:
        """Get ETF holdings information."""

        data = {}
        results = []
        try:
            tbody = self.__soup .find("div", {"id": "holding_section"}).find("tbody")
            holdings = [x for x in tbody.find_all("tr")]
            for record in holdings:
                record_texts = record.find_all("td")
                try:
                    holding_url = self.BASE_URL + record.find("a")["href"]
                except TypeError as e:
                    holding_url = ""
                texts = dict(
                    zip(["Symbol", "Holding", "Share"], [x.text for x in record_texts])
                )
                texts.update({"Url": holding_url})
                results.append(texts)
        except AttributeError:
            results = []

        data["Statistics"] = self._number_of_holdings()
        data["Allocation"] = self._asset_categories()
        data["Holdings"] = results
        return data

    @_try
    def _performance(self) -> dict:
        """Get ETF performance."""
        performance = self.__soup .find("div", {"id": "performance-collapse"}).find("tbody")
        table_rows = [x.text.strip() for x in performance.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    @_try
    def _realtime_rating(self) -> dict:
        """Get realtime ratings of ETF"""
        ratings = self.__soup .find("div", {"id": "realtime-collapse"}).find("table")
        metrics = [x for x in ratings.find_all("tr")]
        results = {}
        for metric in metrics[2:]:
            row = [x.text.strip() for x in metric if x.text.strip() != ""]
            if len(row) == 1:
                row.append(None)
            results[row[0]] = row[1]
        return results

    @_try
    def _technicals(self) -> dict:
        """Get technical analysis indicators for etf."""
        sections = [
            x
            for x in self.__soup .find("div", {"id": "technicals-collapse"}).find_all(
                "ul", class_="list-unstyled"
            )
        ]
        results = []
        for section in sections:
            try:
                results += [s.text.strip().split("\n") for s in section.find_all("li")]
            except (KeyError, TypeError) as e:
                print(e)
        return dict(results)

    @_try
    def _volatility(self):
        """Get Volatility  information."""
        metrics = [
            x.text.strip()
            for x in self.__soup .find("div", {"id": "technicals-collapse"}).find_all(
                "div", class_="row relative-metric-chart"
            )
        ]
        titles = [
            x.text.strip()
            for x in self.__soup .find("div", {"id": "technicals-collapse"}).find_all(
                "div", class_="row relative-metric-header-thumb"
            )
        ]
        return dict(zip(titles, metrics))

    @_try
    def _exposure(self) -> dict:
        """Get ETF exposure information."""
        charts_data = self.__soup .find_all("table", class_="chart base-table")
        if not charts_data:
            return {"Data": "Region, country, sector breakdown data not found"}

        parse_data = []
        chart_series = [x.get("data-chart-series") for x in charts_data]
        chart_titles = [x.get("data-title").replace("<br>", " ") for x in charts_data]
        chart_series_dicts = [json.loads(series) for series in chart_series]
        for chart_dict in chart_series_dicts:
            parse_data.append({x["name"]: x["data"][0] for x in chart_dict})

        return dict(zip(chart_titles, parse_data))


def scrape_etfs(page_size=250, save=False, **kwargs):
    client = ETFDBClient(page_size=page_size)
    etfs = client.scrape_etfs()
    if save:
        dump_json(etfs, "data.json")
    return etfs
