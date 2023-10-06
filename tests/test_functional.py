from contextlib import nullcontext as does_not_raise

import bs4
import pytest

from etfpy import ETF
from etfpy.utils import get_class_property_methods


@pytest.mark.parametrize(
    "example_input,expectation",
    [
        ("SPY", does_not_raise()),
        ("TLT", does_not_raise()),
    ],
)
def test_can_make_soup_request(example_input, expectation):
    """Test how much I know division."""
    with expectation:
        etf = ETF("SPY")
        assert etf is not None and isinstance(etf._soup, bs4.BeautifulSoup)


def test_etf_methods():
    etf = ETF("JEPY")
    method_list = get_class_property_methods(ETF)
    for m in method_list:
        if not m.startswith("_"):
            with does_not_raise():
                data = getattr(etf, m)
                assert isinstance(data, (dict, list))
