from unittest import mock

import pandas as pd
import pytest

from etfpy.analytics.tabular_etf import (
    TabularEquityETFData,
    _BaseTabularETF,
    _mapping,
    etf_to_tabular_wrapper,
)
from etfpy.analytics.utils import (
    clean_data_values_to_float,
    remove_sign_from_values_and_add_as_metric_suffix,
    replace_value_in_df_cell,
)
from etfpy.etf import ETF
from tests.utils import soup


@pytest.fixture(scope="session")
@mock.patch("etfpy.etf.ETF._make_soup_request", soup)
def etf():
    return ETF("JEPY")


@mock.patch("etfpy.etf._ETFDBClient._make_soup_request", soup)
def test_should_properly_wrap_etf_to_tabular_form(etf):
    tabular_df = etf_to_tabular_wrapper(etf)
    assert isinstance(tabular_df, TabularEquityETFData)


@mock.patch("etfpy.etf._ETFDBClient._make_soup_request", soup)
def test_should_tabular_form_have_dataframes_method(etf):
    tabular_df = etf_to_tabular_wrapper(etf)
    assert isinstance(tabular_df.info, pd.DataFrame)
    assert isinstance(tabular_df.info_numeric, pd.DataFrame)
    assert isinstance(tabular_df.volatility, pd.DataFrame)
    assert isinstance(tabular_df.technicals, pd.DataFrame)
    assert isinstance(tabular_df.dividends, pd.DataFrame)
    assert isinstance(tabular_df.exposure_by_region, pd.DataFrame)
    assert isinstance(tabular_df.exposure_by_country, pd.DataFrame)
    assert isinstance(tabular_df.exposure_by_market_cap, pd.DataFrame)


def test_should_properly_create_series(etf):
    tabular = _BaseTabularETF(etf)
    volatility_dict = tabular.etf.volatility
    df = tabular._create_series(volatility_dict)
    assert df.equals(tabular.volatility)


def test_etf_to_tabular_wrapper_properly_provide_class(etf):
    for asset_class, cls in _mapping.items():
        etf.asset_class = asset_class
        tabular_df = etf_to_tabular_wrapper(etf)
        assert isinstance(tabular_df, cls)


@pytest.mark.parametrize(
    "val, expected_result",
    [
        ("1,234.56", 1234.56),
        ("10.5%", 0.10),
        ("10B", 10_000_000_000),
        ("100M", 100_000_000),
        ("1,000K", 1_000_000),
        ("123.45", 123.45),
    ],
)
def test_should_properly_clean_data_values_to_float(val, expected_result):
    actual_result = clean_data_values_to_float(val)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "df, col1, col2, to_replace, expected_result",
    [
        (
            pd.DataFrame(
                {"metric": ["Revenue", "Profit"], "value": ["$100,000", "$50,000"]}
            ),
            "metric",
            "value",
            "$",
            pd.DataFrame(
                {
                    "metric": ["Revenue ($)", "Profit ($)"],
                    "value": ["100,000", "50,000"],
                }
            ),
        ),
        (
            pd.DataFrame(
                {"metric": ["Revenue", "Profit"], "value": ["€100,000", "€50,000"]}
            ),
            "metric",
            "value",
            "€",
            pd.DataFrame(
                {
                    "metric": ["Revenue (€)", "Profit (€)"],
                    "value": ["100,000", "50,000"],
                }
            ),
        ),
        (
            pd.DataFrame(
                {"metric": ["Revenue", "Profit"], "value": ["€100,000", "€50,000"]}
            ),
            "metric",
            "value",
            ["€", "$"],
            pd.DataFrame(
                {
                    "metric": ["Revenue (€)", "Profit (€)"],
                    "value": ["100,000", "50,000"],
                }
            ),
        ),
    ],
)
def test_remove_sign_from_values_and_add_as_metric_suffix(
    df, col1, col2, to_replace, expected_result
):
    actual_result = remove_sign_from_values_and_add_as_metric_suffix(
        df, col1, col2, to_replace
    )
    assert actual_result.equals(expected_result)


@pytest.mark.parametrize(
    "col, to_replace, value, as_type, expected_result",
    [
        (
            pd.Series(["Alice", "Bob", "Carol"]),
            "Alice",
            "John",
            None,
            ["John", "Bob", "Carol"],
        ),
        (
            pd.Series(["50 $", "40 $", "30.5$"]),
            "$",
            "",
            float,
            [50.0, 40.0, 30.5],
        ),
    ],
)
def test_replace_value_in_df_cell_parametrize(
    col, to_replace, value, as_type, expected_result
):
    new_col = replace_value_in_df_cell(col, to_replace, value, as_type)
    assert new_col.tolist() == expected_result
