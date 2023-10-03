from unittest import mock

import bs4
import requests.adapters

from etfpy.utils import (
    _handle_spans,
    chunkify,
    get_headers,
    get_retry_session,
    handle_find_all_rows,
)


@mock.patch(
    "etfpy.utils.user_agent_rotator.get_random_user_agent", lambda: "someuseragent"
)
def test_should_properly_get_headers():
    assert get_headers() == {
        "User-Agent": "someuseragent",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }


def test_should_create_retry_session():
    max_retries = 6
    session = get_retry_session(retries=max_retries)
    for adapter in session.adapters.values():
        assert adapter.max_retries.total == max_retries
        assert isinstance(adapter, requests.adapters.HTTPAdapter)


def test_should_handle_spans():
    html = (
        '[<span class="stock-quote-title">\nPrice:</span>,'
        '<span class="stock-quote-data" id="stock_price_value">$19.68 '
        '<img src="./jepy_files/up.png"/></span>]'
    )
    spans = bs4.BeautifulSoup(html, "html.parser").find_all("span")
    assert _handle_spans(spans) == ("Price:", "$19.68")

    html = '[<div class="stock-quote-title">\nPrice:</div>]'
    spans = bs4.BeautifulSoup(html, "html.parser").find_all("span")
    assert _handle_spans(spans) == ()


def test_handle_find_all_rows():
    soup = bs4.BeautifulSoup(
        "<table id='my_table'><tr><td>1</td><td>a</td></tr><tr><td>2</td><td>b</td></tr></table>",
        "html.parser",
    )
    rows = soup.find_all("tr")
    results = handle_find_all_rows(rows)
    assert results == {"1": "a", "2": "b"}


def test_should_chunkify():
    g = list(range(1, 101))
    results = list(chunkify(g, 10))
    assert len(results) == 10
    assert sum([len(r) for r in results]) == 100
    assert results[-1] == [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
