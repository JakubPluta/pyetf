import bs4
import pytest

from pyetf._clients import ETFDBScraper
from unittest import mock


@pytest.fixture()
def soup():
    return bs4.BeautifulSoup(open("etf.html", encoding="utf8"), "html.parser")


@pytest.fixture()
def etf():
    return ETFDBScraper("VXUS")


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_basic_info(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._basic_info() == {
        "Issuer": "https://etfdb.comhttps://etfdb.com/issuer/vanguard/",
        "Brand": "https://etfdb.comhttps://etfdb.com/issuer/vanguard/",
        "Structure": "ETF",
        "Expense Ratio": "0.08%",
        "ETF Home Page": "https://advisors.vanguard.com/investments/products/vxus/vanguard-total-international-stock-etf",
        "Inception": "Jan 26, 2011",
        "Index Tracked": "https://etfdb.comhttps://etfdb.com/index/vxus-us-ftse-global-all-cap-ex-us-index/",
        "Price:": "$63.97",
        "Change:": "$0.10 (0.16%)",
        "Category:": "Foreign Large Cap Equities",
        "Last Updated:": "Dec 09, 2021",
        "P/E Ratio": "11.30",
        "Open": "$64.00",
        "Volume": "2,410,300",
        "Day Lo": "$64.05",
        "Day Hi": "$64.05",
        "52 Week Lo": "$57.30",
        "52 Week Hi": "$66.76",
        "AUM": "$52,107.0 M",
        "Shares": "811.5 M",
        "Category": "Size and Style",
        "Asset Class": "Equity",
        "Asset Class Size": "Large-Cap",
        "Asset Class Style": "Blend",
        "Region (General)": "Broad Asia",
        "Region (Specific)": "Broad",
        "Segment": "Equity: Global Ex-U.S.  -  Total Market",
        "Focus": "Total Market",
        "Niche": "Broad-based",
        "Strategy": "Vanilla",
        "Weighting Scheme": "Market Cap",
    }


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_technicals(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._technicals() == {
        "20 Day MA": "$64.15",
        "60 Day MA": "$64.51",
        "MACD 15 Period": "0.27",
        "MACD 100 Period": "-0.90",
        "Williams % Range 10 Day": "19.85",
        "Williams % Range 20 Day": "52.81",
        "RSI 10 Day": "50",
        "RSI 20 Day": "47",
        "RSI 30 Day": "47",
        "Ultimate Oscillator": "50",
        "Lower Bollinger (10 Day)": "$61.64",
        "Upper Bollinger (10 Day)": "$64.44",
        "Lower Bollinger (20 Day)": "$61.56",
        "Upper Bollinger (20 Day)": "$66.77",
        "Lower Bollinger (30 Day)": "$62.10",
        "Upper Bollinger (30 Day)": "$67.18",
        "Support Level 1": "$63.76",
        "Support Level 2": "$63.65",
        "Resistance Level 1": "$64.03",
        "Resistance Level 2": "$64.18",
        "Stochastic Oscillator %D (1 Day)": "58.78",
        "Stochastic Oscillator %D (5 Day)": "75.80",
        "Stochastic Oscillator %K (1 Day)": "61.09",
        "Stochastic Oscillator %K (5 Day)": "60.90",
        "Tracking Difference Median (%)": "-0.18",
        "Tracking Difference Max Upside (%)": "-0.04",
        "Tracking Difference Max Downside (%)": "-0.32",
        "Median Premium Discount (%)": "0.15",
        "Maximum Premium Discount (%)": "0.53",
        "Average Spread (%)": "1.00",
        "Average Spread ($)": "1.00",
    }


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_valuation(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._valuation()["P/E Ratio"] == "11.30"


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_dividends(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._dividends() == {
        "Dividend": "$ 0.36",
        "Dividend Date": "2021-09-20",
        "Annual Dividend Rate": "$ 1.62",
        "Annual Dividend Yield": "2.46%",
    }


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_holdings(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._holdings() == {
        "Statistics": {
            "Number of Holdings": "7707",
            "% of Assets in Top 10": "11.01%",
            "% of Assets in Top 15": "13.68%",
            "% of Assets in Top 50": "24.54%",
        },
        "Allocation": {
            "Category": "Foreign Large Cap Equities",
            "Asset Class": "Equity",
            "Asset Class Size": "Large-Cap",
            "Asset Class Style": "Blend",
            "Region (General)": "Broad Asia",
            "Region (Specific)": "Broad",
        },
        "Holdings": [
            {
                "Symbol": "BABA",
                "Holding": "Alibaba Group Holding Ltd",
                "Share": "2.01%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/BABA/",
            },
            {
                "Symbol": "700",
                "Holding": "Tencent Holdings Ltd",
                "Share": "1.50%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/700:HKG/",
            },
            {
                "Symbol": "2330",
                "Holding": "Taiwan Semiconductor Manufacturing Co Ltd",
                "Share": "1.44%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/2330:TAI/",
            },
            {
                "Symbol": "NESN",
                "Holding": "Nestle SA",
                "Share": "1.27%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/NESN:VTX/",
            },
            {
                "Symbol": "005930",
                "Holding": "Samsung Electronics Co Ltd",
                "Share": "1.09%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/005930:KSC/",
            },
            {
                "Symbol": "ROG",
                "Holding": "Roche Holding AG",
                "Share": "0.99%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/ROG:VTX/",
            },
            {
                "Symbol": "NOVN",
                "Holding": "Novartis AG",
                "Share": "0.75%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/NOVN:VTX/",
            },
            {
                "Symbol": "SAP",
                "Holding": "SAP SE",
                "Share": "0.66%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/SAP:DAX/",
            },
            {
                "Symbol": "7203",
                "Holding": "Toyota Motor Corp",
                "Share": "0.65%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/7203:TYO/",
            },
            {
                "Symbol": "ASML",
                "Holding": "ASML Holding NV",
                "Share": "0.61%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/ASML:AEX/",
            },
            {
                "Symbol": "AZN",
                "Holding": "AstraZeneca PLC",
                "Share": "0.58%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/AZN:LSE/",
            },
            {
                "Symbol": "1299",
                "Holding": "AIA Group Ltd",
                "Share": "0.49%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/1299:HKG/",
            },
            {
                "Symbol": "MC",
                "Holding": "LVMH Moet Hennessy Louis Vuitton SE",
                "Share": "0.48%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/MC:PAR/",
            },
            {
                "Symbol": "9984",
                "Holding": "SoftBank Group Corp",
                "Share": "0.47%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/9984:TYO/",
            },
            {
                "Symbol": "3690",
                "Holding": "Meituan Dianping",
                "Share": "0.46%",
                "Url": "https://etfdb.comhttps://etfdb.com/stock/3690:HKG/",
            },
        ],
    }


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_number_of_holdings(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._number_of_holdings() == {
        "Number of Holdings": "7707",
        "% of Assets in Top 10": "11.01%",
        "% of Assets in Top 15": "13.68%",
        "% of Assets in Top 50": "24.54%",
    }


@mock.patch("pyetf._clients.ETFDBScraper._make_soup_request")
def test_performance(mocky, soup, etf):
    mocky.return_value = soup
    assert etf._performance() == {
        "1 Month Return": "-3.36%",
        "3 Month Return": "-3.14%",
        "YTD Return": "7.85%",
        "1 Year Return": "10.44%",
        "3 Year Return": "42.58%",
        "5 Year Return": "57.13%",
    }
