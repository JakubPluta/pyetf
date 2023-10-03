import pandas as pd
from etfpy.etf import ETF


def remove_nested_benchmarks(data: dict, ticker: str):
    results = {}
    for k, v in data.items():
        results[k] = v.get(ticker) if isinstance(v, dict) else v
    return results


class ETFFrame:
    def __init__(self, ticker: str):
        self.etf = ETF(ticker)
        self.ticker = ticker

    def info(self):
        data = pd.Series(
            remove_nested_benchmarks(self.etf.info, self.ticker)
        ).reset_index()
        data.columns = ["metric", "value"]
        return data

    def volatility(self):
        data = pd.Series(self.etf.volatility).reset_index()
        data.columns = ["metric", "value"]
        return data
