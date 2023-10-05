from unittest import mock

import pytest

from etfpy.client._etfs_scraper import ETFListScraper, get_all_etfs


@pytest.fixture
def etf_scraper_client():
    return ETFListScraper()


class ScrapedPage:
    def __init__(self, valid=True):
        self.data = [
            {
                "symbol": {"type": "link", "text": "SPY", "url": "/etf/SPY/"},
                "name": {
                    "type": "link",
                    "text": "SPDR S&P 500 ETF Trust",
                    "url": "/etf/SPY/",
                },
                "mobile_title": "SPY - SPDR S&P 500 ETF Trust",
                "ytd": "12.97%",
                "one_week_return": "-1.14%",
                "fifty_two_week": "21.52%",
                "three_ytd": "9.85%",
                "five_ytd": "9.75%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-4.96%",
            },
            {
                "symbol": {"type": "link", "text": "IVV", "url": "/etf/IVV/"},
                "name": {
                    "type": "link",
                    "text": "iShares Core S&P 500 ETF",
                    "url": "/etf/IVV/",
                },
                "mobile_title": "IVV - iShares Core S&P 500 ETF",
                "ytd": "13.06%",
                "one_week_return": "-1.11%",
                "fifty_two_week": "21.64%",
                "three_ytd": "9.92%",
                "five_ytd": "9.86%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-4.94%",
            },
            {
                "symbol": {"type": "link", "text": "VOO", "url": "/etf/VOO/"},
                "name": {
                    "type": "link",
                    "text": "Vanguard S&P 500 ETF",
                    "url": "/etf/VOO/",
                },
                "mobile_title": "VOO - Vanguard S&P 500 ETF",
                "ytd": "13.09%",
                "one_week_return": "-1.12%",
                "fifty_two_week": "21.61%",
                "three_ytd": "9.93%",
                "five_ytd": "9.81%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-4.95%",
            },
            {
                "symbol": {"type": "link", "text": "VTI", "url": "/etf/VTI/"},
                "name": {
                    "type": "link",
                    "text": "Vanguard Total Stock Market ETF",
                    "url": "/etf/VTI/",
                },
                "mobile_title": "VTI - Vanguard Total Stock Market ETF",
                "ytd": "12.23%",
                "one_week_return": "-1.10%",
                "fifty_two_week": "20.14%",
                "three_ytd": "8.91%",
                "five_ytd": "9.00%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-5.24%",
            },
            {
                "symbol": {"type": "link", "text": "QQQ", "url": "/etf/QQQ/"},
                "name": {
                    "type": "link",
                    "text": "Invesco QQQ Trust Series I",
                    "url": "/etf/QQQ/",
                },
                "mobile_title": "QQQ - Invesco QQQ Trust Series I",
                "ytd": "36.26%",
                "one_week_return": "0.46%",
                "fifty_two_week": "36.09%",
                "three_ytd": "9.24%",
                "five_ytd": "14.97%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-4.19%",
            },
            {
                "symbol": {"type": "link", "text": "VEA", "url": "/etf/VEA/"},
                "name": {
                    "type": "link",
                    "text": "Vanguard FTSE Developed Markets ETF",
                    "url": "/etf/VEA/",
                },
                "mobile_title": "VEA - Vanguard FTSE Developed Markets ETF",
                "ytd": "4.59%",
                "one_week_return": "-2.69%",
                "fifty_two_week": "22.14%",
                "three_ytd": "4.60%",
                "five_ytd": "2.83%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-5.43%",
            },
            {
                "symbol": {"type": "link", "text": "VTV", "url": "/etf/VTV/"},
                "name": {
                    "type": "link",
                    "text": "Vanguard Value ETF",
                    "url": "/etf/VTV/",
                },
                "mobile_title": "VTV - Vanguard Value ETF",
                "ytd": "-0.82%",
                "one_week_return": "-2.51%",
                "fifty_two_week": "13.59%",
                "three_ytd": "12.06%",
                "five_ytd": "7.00%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-4.55%",
            },
            {
                "symbol": {"type": "link", "text": "IEFA", "url": "/etf/IEFA/"},
                "name": {
                    "type": "link",
                    "text": "iShares Core MSCI EAFE ETF",
                    "url": "/etf/IEFA/",
                },
                "mobile_title": "IEFA - iShares Core MSCI EAFE ETF",
                "ytd": "4.83%",
                "one_week_return": "-2.48%",
                "fifty_two_week": "23.34%",
                "three_ytd": "4.46%",
                "five_ytd": "2.71%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-5.23%",
            },
            {
                "symbol": {"type": "link", "text": "BND", "url": "/etf/BND/"},
                "name": {
                    "type": "link",
                    "text": "Vanguard Total Bond Market ETF",
                    "url": "/etf/BND/",
                },
                "mobile_title": "BND - Vanguard Total Bond Market ETF",
                "ytd": "-1.85%",
                "one_week_return": "-1.20%",
                "fifty_two_week": "-0.24%",
                "three_ytd": "-5.54%",
                "five_ytd": "-0.02%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-2.95%",
            },
            {
                "symbol": {"type": "link", "text": "AGG", "url": "/etf/AGG/"},
                "name": {
                    "type": "link",
                    "text": "iShares Core U.S. Aggregate Bond ETF",
                    "url": "/etf/AGG/",
                },
                "mobile_title": "AGG - iShares Core U.S. Aggregate Bond ETF",
                "ytd": "-1.99%",
                "one_week_return": "-1.24%",
                "fifty_two_week": "-0.43%",
                "three_ytd": "-5.56%",
                "five_ytd": "-0.11%",
                "realtime_performance": {"type": "restricted", "url": "/members/join/"},
                "one_month_return": "-3.03%",
            },
        ]
        self.valid = valid

    def json(self):
        if self.valid:
            return {"data": self.data}
        else:
            return {"1": self.data}


def _scrape_page(page, page_size, max_pages=3):
    if page > max_pages:
        return None
    return ScrapedPage().data


@pytest.fixture
def etf_dict():
    return {
        "symbol": {"text": "some_symbol", "url": "/some_url"},
        "name": {"text": "some_name"},
        "ytd": "10%",
        "asset_class": "asset_class",
        "price": "10",
        "average_volume": "10",
    }


@pytest.fixture
def etfs(etf_dict):
    return list(etf_dict for _ in range(10))


def test_can_parse_record(etf_scraper_client, etf_dict):
    assert etf_scraper_client._parse_etf_record(etf_dict) == {
        "symbol": "some_symbol",
        "name": "some_name",
        "url": "https://etfdb.com/some_url",
        "one_year_return": "10%",
        "price": "10",
        "average_volume": "10",
        "asset_class": "asset_class",
    }


def test_can_prepare_etfs_list(etf_scraper_client, etfs):
    assert list(etf_scraper_client._prepare_etfs_list(etfs)) == [
        {
            "symbol": "some_symbol",
            "name": "some_name",
            "url": "https://etfdb.com/some_url",
            "one_year_return": "10%",
            "price": "10",
            "average_volume": "10",
            "asset_class": "asset_class",
        }
        for _ in range(len(etfs))
    ]


@mock.patch("etfpy.client._etfs_scraper.ETFListScraper.post_request")
def test_scrape_page(m, etf_scraper_client):
    fake_page = ScrapedPage()
    m.return_value = fake_page
    page = etf_scraper_client._scrape_page(1, 10)
    assert page == fake_page.data

    invalid_page = ScrapedPage(valid=False)
    m.return_value = invalid_page
    page = etf_scraper_client._scrape_page(1, 10)
    assert page == []


def test_should_get_etfs(etf_scraper_client):
    etf_scraper_client._scrape_page = _scrape_page
    results = list(etf_scraper_client.get_etfs(10))
    assert len(results) == 3 and len(results[0]) == 10


@mock.patch("etfpy.client._etfs_scraper.ETFListScraper.get_etfs")
def test_get_all_etfs(m):
    data = ScrapedPage().data
    rng = 10
    m.return_value = (data for _ in range(rng))
    assert len(get_all_etfs()) == len(data * rng)
