from unittest import mock

import bs4
import requests.adapters

from etfpy.utils import (
    _handle_nth_child,
    _handle_spans,
    chunkify,
    get_class_property_methods,
    get_headers,
    get_retry_session,
    handle_find_all_rows,
    handle_tbody_thead,
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
    assert _handle_spans("something") is None


def test_handle_find_all_rows():
    soup = bs4.BeautifulSoup(
        "<table id='my_table'><tr><td>1</td><td>a</td></tr><tr><td>2</td><td>b</td></tr></table>",
        "html.parser",
    )
    rows = soup.find_all("tr")
    results = handle_find_all_rows(rows)
    assert results == {"1": "a", "2": "b"}


def test_should_properly_chunkify():
    g = list(range(1, 101))
    results = list(chunkify(g, 10))
    assert len(results) == 10
    assert sum([len(r) for r in results]) == 100
    assert results[-1] == [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def test_should_properly_handle_tbody_thead():
    soup = bs4.BeautifulSoup(
        "<table id='my_table'><thead><tr><th>Size</th><th>Value</th></tr>"
        "</thead><tbody><tr><td>Small</td><td>10</td></tr><tr><td>Medium</td><td>20</td>"
        "</tr><tr><td>Large</td><td>30</td></tr></tbody></table>",
        "html.parser",
    )
    assert handle_tbody_thead(soup, table_id="my_table") == {
        "Large": {"Value": "30"},
        "Small": {"Value": "10"},
    }


def test_should_get_property_methods():
    class Foo:
        @property
        def is_property(self):
            return 1

        def not_property(self):
            return 0

    r = get_class_property_methods(Foo)
    assert r == ["is_property"]


def test_should_handle_nth_span():
    soup = bs4.BeautifulSoup(
        "<table id='my_table'><tr><td>1</td><td>a</td></tr><tr><td>2</td><td>b</td></tr></table>",
        "html.parser",
    ).find("tr")
    assert _handle_nth_child(soup, 1) == "1"
    assert _handle_nth_child(5, 12) is None
