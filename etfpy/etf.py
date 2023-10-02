from etfpy.client.etf_client import ETFDBClient as _ETFDBClient
from etfpy.utils import get_class_property_methods


class ETF(_ETFDBClient):
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


def load_etf(etf: str) -> ETF:
    return ETF(etf)


__all__ = ["ETF", "load_etf"]
