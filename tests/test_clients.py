import os.path

import bs4
import pytest

from etfpy.clients.etfdb_client import ETFDBClient
from unittest import mock
from pathlib import Path

here = Path(__file__).parent


@pytest.fixture(scope="session")
def soup():
    with open(os.path.join(here, "jepy.html"), encoding="utf8") as f:
        data = bs4.BeautifulSoup(f, "html.parser")
    return data


@pytest.fixture(scope="session")
def etf():
    return ETFDBClient("JEPY")


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_basic_info(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._basic_info() == {
        "Symbol": "JEPY",
        "Url": "https://etfdb.com/etf/JEPY",
        "Issuer": "https://etfdb.com/issuer/tidal/",
        "Brand": "https://etfdb.com/issuer/defiance/",
        "Expense Ratio": "0.99%",
        "Inception": "Sep 18, 2023",
        "Index Tracked": "ACTIVE - No Index",
        "Price:": "$19.61",
        "Change:": "$0.1 (0.01%)",
        "Category:": "n/a",
        "Last Updated:": "Sep 28, 2023",
        "P/E Ratio": {
            "JEPY": "N/A",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "5.86",
        },
        "52 Week Lo": "$19.33",
        "52 Week Hi": "$20.12",
        "AUM": "$0.0 M",
        "Shares": "0.0 M",
        "Category": "Size and Style",
        "Asset Class": "Equity",
        "Segment": "Equity: U.S.  -  Large Cap",
        "Focus": "Large Cap",
        "Niche": "Broad-based",
        "Strategy": "Active",
        "Weighting Scheme": "Proprietary",
    }


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_technicals(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._technicals() == {
        "20 Day MA": "n/a",
        "60 Day MA": "n/a",
        "MACD 15 Period": "n/a",
        "MACD 100 Period": "n/a",
        "Williams % Range 10 Day": "n/a",
        "Williams % Range 20 Day": "n/a",
        "RSI 10 Day": "n/a",
        "RSI 20 Day": "n/a",
        "RSI 30 Day": "n/a",
        "Ultimate Oscillator": "n/a",
        "Lower Bollinger (10 Day)": "n/a",
        "Upper Bollinger (10 Day)": "n/a",
        "Lower Bollinger (20 Day)": "n/a",
        "Upper Bollinger (20 Day)": "n/a",
        "Lower Bollinger (30 Day)": "n/a",
        "Upper Bollinger (30 Day)": "n/a",
        "Support Level 1": "$19.50",
        "Support Level 2": "$19.40",
        "Resistance Level 1": "$19.67",
        "Resistance Level 2": "$19.74",
        "Stochastic Oscillator %D (1 Day)": "65.94",
        "Stochastic Oscillator %D (5 Day)": "38.69",
        "Stochastic Oscillator %K (1 Day)": "52.03",
        "Stochastic Oscillator %K (5 Day)": "n/a",
        "Tracking Difference Median (%)": "n/a",
        "Tracking Difference Max Upside (%)": "n/a",
        "Tracking Difference Max Downside (%)": "n/a",
        "Median Premium Discount (%)": "0.19",
        "Maximum Premium Discount (%)": "0.33",
        "Average Spread (%)": "3.72",
        "Average Spread ($)": "3.72",
    }


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_valuation(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._valuation()["P/E Ratio"] == {
        "ETF Database Category Average": "N/A",
        "FactSet Segment Average": "5.86",
        "JEPY": "N/A",
    }


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_dividends(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._dividends() == {
        "Dividend": {
            "JEPY": "N/A",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "$ 0.16",
        },
        "Dividend Date": {
            "JEPY": "N/A",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "N/A",
        },
        "Annual Dividend Rate": {
            "JEPY": "N/A",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "$ 0.62",
        },
        "Annual Dividend Yield": {
            "JEPY": "N/A",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "1.37%",
        },
    }


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_holdings(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._holdings() == {
        "Statistics": {
            "Number of Holdings": {
                "JEPY": "3",
                "ETF Database Category Average": "N/A",
                "FactSet Segment Average": "174",
            },
            "% of Assets in Top 10": {
                "JEPY": "100.00%",
                "ETF Database Category Average": "N/A",
                "FactSet Segment Average": "58.76%",
            },
            "% of Assets in Top 15": {
                "JEPY": "100.00%",
                "ETF Database Category Average": "N/A",
                "FactSet Segment Average": "63.43%",
            },
            "% of Assets in Top 50": {
                "JEPY": "100.00%",
                "ETF Database Category Average": "N/A",
                "FactSet Segment Average": "80.52%",
            },
        },
        "Allocation": {"Category": "n/a", "Asset Class": "Equity"},
        "Holdings": [
            {"Symbol": "N/A", "Holding": "U.S. Dollar", "Share": "98.89%", "Url": ""},
            {
                "Symbol": "FGXXX",
                "Holding": "First American Funds Inc X Government Obligations Fund",
                "Share": "1.35%",
                "Url": "https://etfdb.com/stock/FGXXX/",
            },
            {"Symbol": "N/A", "Holding": "OPTIONS", "Share": "-0.24%", "Url": ""},
        ],
    }


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_number_of_holdings(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._number_of_holdings() == {
        "Number of Holdings": {
            "JEPY": "3",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "174",
        },
        "% of Assets in Top 10": {
            "JEPY": "100.00%",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "58.76%",
        },
        "% of Assets in Top 15": {
            "JEPY": "100.00%",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "63.43%",
        },
        "% of Assets in Top 50": {
            "JEPY": "100.00%",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "80.52%",
        },
    }


@mock.patch("etfpy.clients.etfdb_client.ETFDBClient._make_soup_request")
def test_performance(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._performance() == {
        "1 Month Return": {
            "JEPY": "-1.96%",
            "ETF Database\n\nCategory Average": "-1.38%",
            "Factset Segment\n\nAverage": "-1.51%",
        },
        "3 Month Return": {
            "JEPY": "-1.96%",
            "ETF Database\n\nCategory Average": "-1.85%",
            "Factset Segment\n\nAverage": "-0.99%",
        },
        "YTD Return": {
            "JEPY": "N/A",
            "ETF Database\n\nCategory Average": "3.13%",
            "Factset Segment\n\nAverage": "6.94%",
        },
        "1 Year Return": {
            "JEPY": "N/A",
            "ETF Database\n\nCategory Average": "2.55%",
            "Factset Segment\n\nAverage": "9.70%",
        },
        "3 Year Return": {
            "JEPY": "N/A",
            "ETF Database\n\nCategory Average": "0.09%",
            "Factset Segment\n\nAverage": "4.35%",
        },
        "5 Year Return": {
            "JEPY": "N/A",
            "ETF Database\n\nCategory Average": "0.03%",
            "Factset Segment\n\nAverage": "2.08%",
        },
    }
