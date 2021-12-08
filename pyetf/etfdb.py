import functools
import json
import os
import re

import bs4
import requests


class InvalidETFException(Exception):
    pass


def load_ticker_list() -> list:
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "etfdb.json"
    )
    with open(path, "r") as f:
        data = json.load(f)
    return data


tickers: list = [etf.get("symbol") for etf in load_ticker_list()]


class ETFDBScraper:
    BASE_URL = "https://etfdb.com"
    CATEGORIES = {
        "profile": "#etf-ticker-profile",
        "valuation": "#etf-ticker-valuation-dividend",
        "expense": "#expense",
        "holdings": "#holdings",
        "performance": "#performance",
        "technicals": "#technicals",
        "rating": "#realtime-rating",
    }

    def __init__(self, ticker: str):
        if ticker.upper() in tickers:
            self.ticker = ticker.upper()
        else:
            raise InvalidETFException(f"{ticker} doesn't exist in ETF Database\n")

    def _prepare_url(self, category=None):
        url = f"{self.BASE_URL}/etf/{self.ticker}/"
        if category and category in self.CATEGORIES:
            url += self.CATEGORIES.get(category)
        return url

    @functools.lru_cache(maxsize=128)
    def _make_soup_request(self, category):
        url = self._prepare_url(category)
        response = requests.get(url)
        return bs4.BeautifulSoup(response.text, "html.parser")

    def vitals_section(self):
        soup = self._make_soup_request("profile")
        etf_ticker_body = soup.find("div", {"id": "etf-ticker-body"}).find(
            "div", class_="row"
        )
        vitals = {
            i.select_one(":nth-child(1)")
            .text.strip(): i.select_one(":nth-child(2)")
            .text.strip()
            for i in etf_ticker_body.find_all("div", class_="row")
        }
        vitals.update({"Analyst Report": etf_ticker_body.find("p").text.strip()})
        return vitals

    def database_theme(self):
        soup = self._make_soup_request("profile")
        theme = soup.find("div", {"id": "etf-ticker-body"}).find_all(
            "div", class_="ticker-assets"
        )[1]
        theme_dict = {
            i.select_one(":nth-child(1)")
            .text.strip(): i.select_one(":nth-child(2)")
            .text.strip()
            for i in theme.find_all("div", class_="row")
        }
        return theme_dict

    def factset_classification(self):
        soup = self._make_soup_request("profile")
        factset = soup.find("div", {"id": "factset-classification"}).find_all("li")
        factset_dict = {
            i.select_one(":nth-child(1)")
            .text.strip(): i.select_one(":nth-child(2)")
            .text.strip()
            for i in factset
        }
        return factset_dict

    def trading_data(self):
        # TODO: OHLC is empty ?
        soup = self._make_soup_request("profile")
        trading_data = soup.find(
            "div", {"class": "data-trading bar-charts-table"}
        ).find_all("li")
        trading_dict = {
            i.select_one(":nth-child(1)")
            .text.strip(): i.select_one(":nth-child(2)")
            .text.strip()
            for i in trading_data
        }
        return trading_dict

    def valuation(self):
        regex = re.compile(".*h4 center.*")
        soup = self._make_soup_request("valuation")
        valuation = (
            soup.find("div", {"id": "etf-ticker-valuation-dividend"})
            .find("div", {"id": "valuation"})
            .find_all("div", class_="row")
        )
        values = [x.text for x in valuation[1].find_all("div", class_="text-center")]
        titles = [x.text for x in valuation[1].find_all("div", class_=regex)]
        results = dict(
            zip(titles, [{values[i], values[i + 1]} for i in range(len(values) // 2)])
        )
        return results

    def dividends(self):
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
                    results[category][data_th] = text
        return results

    def expenses(self):
        soup = self._make_soup_request("expense")
        exp = soup.find("div", {"id": "etf-ticker-body"}).find("div", {"id": "expense"})
        tag = [
            x for x in exp.find_all("div", class_="row")[0] if isinstance(x, bs4.Tag)
        ]
        text = [x.find_all("div", class_="text-center")[:2] for x in tag][0]
        return {text[0].text: text[1].text}

    def holdings(self):
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
        return results

    def number_of_holdings(self):
        soup = self._make_soup_request("holdings")
        holdings_table = soup.find("table", {"id": "holdings-table"}).find("tbody")
        table_rows = [x.text.strip() for x in holdings_table.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    def size_locations(self):
        soup = self._make_soup_request("holdings")
        size_locations = soup.find("table", {"id": "size-table"}).find("tbody")
        table_rows = [x.text.strip() for x in size_locations.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    def performance(self):
        soup = self._make_soup_request("performance")
        performance = soup.find("div", {"id": "performance-collapse"}).find("tbody")
        table_rows = [x.text.strip() for x in performance.find_all("td")]
        results = {}
        for i in range(0, len(table_rows), 4):
            results[table_rows[i]] = table_rows[i + 1]
        return results

    def realtime_rating(self):
        soup = self._make_soup_request("rating")
        ratings = soup.find("div", {"id": "realtime-collapse"}).find("table")
        metrics = [x for x in ratings.find_all("tr")]
        results = {}
        for metric in metrics[2:]:
            row = [x.text.strip() for x in metric if x.text.strip() != ""]
            results[row[0]] = row[1]
        return results

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

