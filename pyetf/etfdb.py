import functools
import json
import os
import re

import bs4
import requests
from utils import _try

__docformat__ = "numpy"


class InvalidETFException(Exception):
    """Invalid ETF Exception class"""


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
    CATEGORIES = {
        "profile": "#etf-ticker-profile",
        "valuation": "#etf-ticker-valuation-dividend",
        "expense": "#expense",
        "holdings": "#holdings",
        "performance": "#performance",
        "technicals": "#technicals",
        "rating": "#realtime-rating",
        "charts": "#charts",
    }

    def __init__(self, ticker: str):
        if ticker.upper() in tickers:
            self.ticker = ticker.upper()
            self.ticker_data = tickers.get(self.ticker)
        else:
            raise InvalidETFException(f"{ticker} doesn't exist in ETF Database\n")

    def _prepare_url(self, category=None) -> str:
        """Builds url for given category and ticker.

        Parameters
        ----------
        category: str
            One from list ["profile", "valuation", "expense", "holdings", "performance", "technicals", "rating"]

        Returns
        -------
        str: prepared url for request.
        """

        url = f"{self.BASE_URL}/etf/{self.ticker}/"
        if category and category in self.CATEGORIES:
            url += self.CATEGORIES.get(category)
        return url

    @functools.lru_cache(maxsize=128)
    def _make_soup_request(self, category: str) -> bs4.BeautifulSoup:
        """Make GET request to etfdb.com, and put response into BeautifulSoup data structure.

        Parameters
        ----------
        category: str
            One from list ["profile", "valuation", "expense", "holdings", "performance", "technicals", "rating"]

        Returns
        -------
        BeautifulSoup object ready to parse with bs4 library
        """

        url = self._prepare_url(category)
        response = requests.get(url)
        return bs4.BeautifulSoup(response.text, "html.parser")

    @_try
    def _get_profile_container(self, soup: bs4.BeautifulSoup = None) -> dict:
        """Parse profile-container div into dictionary with base statistics.

        Returns
        -------
        dict:
            ETF profile statistics
        """

        if not soup:
            soup = self._make_soup_request("profile")
        profile_container = [
            x.find_all("span")
            for x in soup.find("div", {"class": "profile-container"}).find_all(
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
    def _trading_data(self, soup: bs4.BeautifulSoup = None) -> dict:
        """Parse data-trading div into dict

        Returns
        -------
        dict:
            ETF trading information
        """
        if not soup:
            soup = self._make_soup_request("profile")
        trading_data = soup.find(
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
    def _asset_categories(self, soup: bs4.BeautifulSoup = None) -> dict:
        """Parse data-trading div into dict

        Returns
        -------
        dict:
            ETF trading information
        """
        if not soup:
            soup = self._make_soup_request("profile")
        theme = soup.find("div", {"id": "etf-ticker-body"}).find_all(
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
    def _factset_classification(self, soup: bs4.BeautifulSoup = None) -> dict:
        """Parse factset information

        Returns
        -------
        dict:
            ETF factset information
        """

        if not soup:
            soup = self._make_soup_request("profile")
        factset = soup.find("div", {"id": "factset-classification"}).find_all("li")
        factset_dict = {
            li.select_one(":nth-child(1)")
            .text.strip(): li.select_one(":nth-child(2)")
            .text.strip()
            for li in factset
        }
        return factset_dict

    @_try
    def _number_of_holdings(self) -> dict:
        """Get number of holdings for given etf

        Returns
        -------
        dict:
            Number of etf holdings
        """

        soup = self._make_soup_request("holdings")
        holdings_table = soup.find("table", {"id": "holdings-table"}).find("tbody")
        table_rows = [x.text.strip() for x in holdings_table.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    @_try
    def _size_locations(self) -> dict:
        """Get size allocations of holdings for given etf

        Returns
        -------
        dict:
            Number of etf holdings
        """
        soup = self._make_soup_request("holdings")
        size_locations = soup.find("table", {"id": "size-table"}).find("tbody")
        table_rows = [x.text.strip() for x in size_locations.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    @_try
    def basic_info(self):
        """
        Return basic information about ETF. Like:
            - Issuer, Brand, Expense Ration, Home Page, Inception, Index

        Returns
        -------
        dict:
            ETF basic information
        """

        soup = self._make_soup_request("profile")
        etf_ticker_body = soup.find("div", {"id": "etf-ticker-body"}).find(
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

        basic_information.update(self._get_profile_container(soup))
        basic_information.update(self._trading_data(soup))
        basic_information.update(self._asset_categories(soup))
        basic_information.update(self._factset_classification(soup))
        if "Analyst Report" in basic_information:
            basic_information.pop("Analyst Report")
        return basic_information

    @_try
    def valuation(self) -> dict:
        """Get ETF valuation metrics.

        Returns
        -------
        dict:
            ETF valuation
        """

        soup = self._make_soup_request("valuation")
        valuation = (
            soup.find("div", {"id": "etf-ticker-valuation-dividend"})
            .find("div", {"id": "valuation"})
            .find_all("div", class_="row")
        )
        values = [
            div.text for div in valuation[1].find_all("div", class_="text-center")
        ]
        return {values[0]: values[1]}

    @_try
    def dividends(self) -> dict:
        """Get ETF dividend information.

        Returns
        -------
        dict:
            ETF dividend
        """

        soup = self._make_soup_request("valuation")
        results = {}
        dividend = (
            soup.find("div", {"id": "etf-ticker-valuation-dividend"})
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
    def holdings(self) -> dict:
        """Get ETF holdings information.

        Returns
        -------
        dict:
            ETF Holdings
        """
        data = {}
        soup = self._make_soup_request("holdings")
        results = []
        tbody = soup.find("div", {"id": "holding_section"}).find("tbody")
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

        data["Statistics"] = self._number_of_holdings()
        data["Allocation"] = self._asset_categories()
        data["Holdings"] = results
        return data

    @_try
    def performance(self) -> dict:
        """Get ETF performance.

        Returns
        -------
        dict:
            ETF performance
        """

        soup = self._make_soup_request("performance")
        performance = soup.find("div", {"id": "performance-collapse"}).find("tbody")
        table_rows = [x.text.strip() for x in performance.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    @_try
    def realtime_rating(self):
        soup = self._make_soup_request("rating")
        ratings = soup.find("div", {"id": "realtime-collapse"}).find("table")
        metrics = [x for x in ratings.find_all("tr")]
        results = {}
        for metric in metrics[2:]:
            row = [x.text.strip() for x in metric if x.text.strip() != ""]
            if len(row) == 1:
                row.append(None)
            results[row[0]] = row[1]
        return results

    @_try
    def technicals(self):
        soup = self._make_soup_request("technicals")
        sections = [
            x
            for x in soup.find("div", {"id": "technicals-collapse"}).find_all(
                "ul", class_="list-unstyled"
            )
        ]
        results = []
        for section in sections:
            results += [s.text.strip().split("\n") for s in section.find_all("li")]
        return dict(results)

    @_try
    def volatility(self):
        soup = self._make_soup_request("technicals")
        metrics = [
            x.text.strip()
            for x in soup.find("div", {"id": "technicals-collapse"}).find_all(
                "div", class_="row relative-metric-chart"
            )
        ]
        titles = [
            x.text.strip()
            for x in soup.find("div", {"id": "technicals-collapse"}).find_all(
                "div", class_="row relative-metric-header-thumb"
            )
        ]
        return dict(zip(titles, metrics))

    @_try
    def exposure(self):
        soup = self._make_soup_request("charts")
        charts_data = soup.find_all("table", class_="chart base-table")
        if not charts_data:
            return {"Data": "Region, country, sector breakdown data not found"}

        parse_data = []
        chart_series = [x.get("data-chart-series") for x in charts_data]
        chart_titles = [x.get("data-title").replace("<br>", " ") for x in charts_data]
        chart_series_dicts = [json.loads(series) for series in chart_series]
        for chart_dict in chart_series_dicts:
            parse_data.append({x["name"]: x["data"][0] for x in chart_dict})

        return dict(zip(chart_titles, parse_data))
