from unittest import mock

from etfpy.client.etf_client import ETFDBClient
from tests.utils import soup


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_basic_info():
    etf = ETFDBClient("JEPY")
    assert etf._basic_info() == {
        "Symbol": "JEPY",
        "Url": "https://etfdb.com/etf/JEPY",
        "Issuer": "https://etfdb.com/issuer/tidal/",
        "Brand": "https://etfdb.com/issuer/defiance/",
        "Expense Ratio": "0.99%",
        "Inception": "Sep 18, 2023",
        "Index Tracked": "ACTIVE - No Index",
        "Price:": "$19.68",
        "Change:": "$0.07 (0.36%)",
        "Category:": "n/a",
        "Last Updated:": "Sep 28, 2023",
        "P/E Ratio": {
            "JEPY": "N/A",
            "ETF Database Category Average": "N/A",
            "FactSet Segment Average": "5.86",
        },
        "Open": "$19.83",
        "Volume": "411,400",
        "Day Lo": "$19.86",
        "Day Hi": "$19.86",
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
        "Analyst Report": "https://etfdb.com/advisor_reports/JEPY/",
    }


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_technicals():
    etf = ETFDBClient("JEPY")
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


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_valuation():
    etf = ETFDBClient("JEPY")
    assert etf._valuation()["P/E Ratio"] == {
        "ETF Database Category Average": "N/A",
        "FactSet Segment Average": "5.86",
        "JEPY": "N/A",
    }


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_dividends():
    etf = ETFDBClient("JEPY")
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


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_holdings():
    etf = ETFDBClient("JEPY")
    assert etf._holdings() == [
        {"Symbol": "N/A", "Holding": "U.S. Dollar", "Share": "98.89%", "Url": ""},
        {
            "Symbol": "FGXXX",
            "Holding": "First American Funds Inc X Government Obligations Fund",
            "Share": "1.35%",
            "Url": "https://etfdb.com/stock/FGXXX/",
        },
        {"Symbol": "N/A", "Holding": "OPTIONS", "Share": "-0.24%", "Url": ""},
    ]


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_number_of_holdings():
    etf = ETFDBClient("JEPY")
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


@mock.patch("etfpy.client.etf_client.ETFDBClient._make_soup_request", soup)
def test_performance():
    etf = ETFDBClient("JEPY")
    assert etf._performance() == {
        "1 Month Return": {
            "JEPY": "-1.96%",
            "ETF Database Category Average": "-1.38%",
            "Factset Segment Average": "-1.51%",
        },
        "3 Month Return": {
            "JEPY": "-1.96%",
            "ETF Database Category Average": "-1.85%",
            "Factset Segment Average": "-0.99%",
        },
        "YTD Return": {
            "JEPY": "N/A",
            "ETF Database Category Average": "3.13%",
            "Factset Segment Average": "6.94%",
        },
        "1 Year Return": {
            "JEPY": "N/A",
            "ETF Database Category Average": "2.55%",
            "Factset Segment Average": "9.70%",
        },
        "3 Year Return": {
            "JEPY": "N/A",
            "ETF Database Category Average": "0.09%",
            "Factset Segment Average": "4.35%",
        },
        "5 Year Return": {
            "JEPY": "N/A",
            "ETF Database Category Average": "0.03%",
            "Factset Segment Average": "2.08%",
        },
    }
