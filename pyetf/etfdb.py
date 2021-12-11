from pyetf._clients import ETFDBScraper, tickers, InvalidETFException
from pyetf.utils import get_class_property_methods


def list_etfs():
    return list(tickers.keys())


class ETF(ETFDBScraper):
    """ETF Client"""

    def __init__(self, ticker: str):
        super().__init__(ticker)

    @property
    def info(self):
        return self._basic_info()

    @property
    def holdings(self):
        return self._holdings()

    @property
    def exposure(self):
        return self._exposure()

    @property
    def volatility(self):
        return self._volatility()

    @property
    def technicals(self):
        return self._technicals()

    @property
    def ratings(self):
        return self._realtime_rating()

    @property
    def performance(self):
        return self._performance()

    @property
    def dividends(self):
        return self._dividends()

    def to_dict(self):
        data = {}
        method_list = get_class_property_methods(self.__class__)
        for m in method_list:
            data[m.title()] = getattr(self, m)
        return data


def load_etf(ticker: str) -> ETF:
    if ticker.upper() not in tickers:
        raise InvalidETFException(f"{ticker} doesn't exist in ETF Database\n")
    return ETF(ticker.upper())


def get_raw_etf_dict(ticker: str) -> dict:
    etf = load_etf(ticker)
    return etf.to_dict()
