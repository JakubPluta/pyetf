from typing import Union

import pandas as pd

from etfpy.analytics.utils import (
    remove_sign_from_values_and_add_as_metric_suffix,
    replace_value_in_df_cell,
    clean_data_values_to_float,
)
from etfpy.deco import lowercase_and_underscore_column_names
from etfpy.log import get_logger
from etfpy.utils import remove_nested_benchmarks

logger = get_logger()


class _BaseTabularETF:
    def __init__(self, etf):
        self.etf = etf

    def _create_series(self, data: dict) -> pd.Series:
        """Creates a pandas Series from the given data dictionary.

        Parameters:
        -----------
        data: dict
            A dictionary of data.

        Returns:
        -----------
            A pandas Series object.
        """
        try:
            df = (
                pd.Series(remove_nested_benchmarks(data, self.etf.ticker))
                .reset_index()
                .replace({r"(?i)N/A": None}, regex=True)
            )
            df.columns = ["metric", "value"]
        except (ValueError, TypeError, AttributeError) as vtae:
            logger.warning("couldn't create series from data dict %s", str(vtae))
            df = pd.Series()
        return df

    @lowercase_and_underscore_column_names
    def _create_data_frame(self, data) -> pd.DataFrame:
        return pd.DataFrame(data).replace({r"(?i)N/A": None}, regex=True)

    @classmethod
    def from_etf(cls, etf):
        """Creates a new instance of the class from the given ETF object.

        Parameters:
        -----------
        etf: An ETF object.

        Returns:
        -----------
            A new instance of the class.
        """

        return cls(etf=etf)

    @property
    def holdings(self):
        """Returns a pandas DataFrame of the ETF's holdings."""
        df = self._create_data_frame(self.etf.holdings)
        df["share"] = replace_value_in_df_cell(df["share"], "%", "", float)
        return df.rename(columns={"share": "%_share"})

    @property
    def performance(self):
        """Returns a pandas DataFrame of the ETF's performance."""
        df = self._create_data_frame(self.etf.performance)
        df.columns = [f"%_{c}" for c in df.columns]
        for col in df.columns:
            df[col] = replace_value_in_df_cell(df[col], "%", "", float)
        return df

    @property
    def dividends(self):
        """Returns a pandas DataFrame of the ETF's dividends."""
        df = self._create_data_frame(self.etf.dividends)
        _map = {
            "annual_dividend_yield": "%",
            "annual_dividend_rate": "$",
            "dividend": "$",
        }
        for col, to_replace in _map.items():
            df[col] = replace_value_in_df_cell(df[col], to_replace, "", float)
        return df.rename(columns={"annual_dividend_rate": "%_annual_dividend_rate"})

    @property
    def holding_statistics(self):
        """Returns a pandas DataFrame of the ETF's holding statistics."""
        df = self._create_data_frame(self.etf.holding_statistics)
        for col in df.columns:
            df[col] = replace_value_in_df_cell(df[col], "%", "", float)
        return df

    @property
    def info(self):
        """Returns a pandas Series of the ETF's information."""
        columns = [
            "Symbol",
            "Url",
            "Issuer",
            "Brand",
            "Inception",
            "Index Tracked",
            "Last Updated:",
            "Category",
            "Asset Class",
            "Segment",
            "Focus",
            "Niche",
            "Strategy",
            "Weighting Scheme",
        ]
        data = {
            k[:-1] if k.endswith(":") else k: v
            for k, v in self.etf.info.items()
            if k in columns
        }
        df = self._create_series(data)
        df = remove_sign_from_values_and_add_as_metric_suffix(df)
        return df

    @property
    def info_numeric(self):
        columns = [
            "Expense Ratio",
            "Price:",
            "Change:",
            "P/E Ratio",
            "52 Week Lo",
            "52 Week Hi",
            "AUM",
            "Shares",
        ]
        data = {
            k[:-1] if k.endswith(":") else k: v
            for k, v in self.etf.info.items()
            if k in columns
        }
        try:
            change = data["Change"]
            change_val, *_ = change.split(" ")
            data["Change"] = change_val
        except (IndexError, AttributeError, KeyError) as iak:
            logger.warning("couldn't extract change information: %s", str(iak))
        df = self._create_series(data)
        df = remove_sign_from_values_and_add_as_metric_suffix(df, to_replace=["$", "%"])
        df["value"] = df["value"].apply(lambda x: clean_data_values_to_float(x))
        return df

    @property
    def volatility(self):
        """Returns a pandas Series of the ETF's volatility."""
        return self._create_series(self.etf.volatility)

    @property
    def asset_categories(self):
        """Returns a pandas Series of the ETF's asset categories."""

        return self._create_series(self.etf.asset_categories)

    @property
    def technicals(self):
        """Returns a pandas Series of the ETF's technicals."""
        df = self._create_series(self.etf.technicals)
        df = remove_sign_from_values_and_add_as_metric_suffix(df)
        return df

    def __repr__(self):
        """Returns a string representation of the object."""

        return f"{self.__class__.__name__}(ticker={self.etf.ticker})(asset_class={self.etf.asset_class})"


class _OthersExposureMixin:
    """
    Mixin class that provides access to ETF exposure data.

    This mixin class provides access to the following ETF exposure data:

    * Asset allocation
    * Country breakdown
    * Market cap breakdown
    * Region breakdown
    * Sector breakdown

    Each of these exposure data points is represented as a pandas Series object.
    """

    @property
    def exposure_by_asset(self):
        """Returns a pandas Series of the ETF's exposure by asset."""

        return self._create_series(self.etf.exposure.get("Asset Allocation"))

    @property
    def exposure_by_country(self):
        """Returns a pandas Series of the ETF's exposure by country."""

        return self._create_series(self.etf.exposure.get("Country Breakdown"))

    @property
    def exposure_by_market_cap(self):
        """Returns a pandas Series of the ETF's exposure by market cap."""

        return self._create_series(self.etf.exposure.get("Market Cap Breakdown"))

    @property
    def exposure_by_region(self):
        """Returns a pandas Series of the ETF's exposure by region."""

        return self._create_series(self.etf.exposure.get("Region Breakdown"))

    @property
    def exposure_by_sector(self):
        """Returns a pandas Series of the ETF's exposure by sector."""

        return self._create_series(self.etf.exposure.get("Sector Breakdown"))


class _BondExposureMixin:
    """
    Mixin class that provides access to bond exposure data.

    This mixin class provides access to the following bond exposure data:

    * Asset allocation
    * Maturity breakdown
    * Bond sector breakdown

    Each of these exposure data points is represented as a pandas Series object.
    """

    @property
    def exposure_by_asset(self):
        """Returns a pandas Series of the bond ETF's exposure by asset."""

        return self._create_series(self.etf.exposure.get("Asset Allocation"))

    @property
    def exposure_by_maturity(self):
        """Returns a pandas Series of the bond ETF's exposure by maturity."""

        return self._create_series(self.etf.exposure.get("Maturity Breakdown"))

    @property
    def exposure_by_bond_sector(self):
        """Returns a pandas Series of the bond ETF's exposure by bond sector."""

        return self._create_series(self.etf.exposure.get("Bond Sector Breakdown"))


class TabularAlternativesETFData(_BaseTabularETF):
    """Tabular data for alternatives ETFs.

    This class provides access to the following tabular ETF data:

    * Holdings
    * Performance
    * Dividends
    * Holding statistics
    * Info
    * Volatility
    * Asset categories
    * Technicals

    Each of these data points is provided in the form of pandas DataFrames and Series.
    """


class TabularCurrencyETFData(_BaseTabularETF):
    """Tabular data for currency ETFs.

    This class provides access to the following tabular ETF data:

    * Holdings
    * Performance
    * Dividends
    * Holding statistics
    * Info
    * Volatility
    * Asset categories
    * Technicals

    Each of these data points is provided in the form of pandas DataFrames and Series.
    """


class TabularPreferredStockETFData(_BaseTabularETF):
    """Tabular data for preferred stock ETFs.

    This class provides access to the following tabular ETF data:

    * Holdings
    * Performance
    * Dividends
    * Holding statistics
    * Info
    * Volatility
    * Asset categories
    * Technicals

    Each of these data points is provided in the form of pandas DataFrames and Series.
    """


class TabularVolatilityETFData(_BaseTabularETF):
    """Tabular data for volatility ETFs.

    This class provides access to the following tabular ETF data:

    * Holdings
    * Performance
    * Dividends
    * Holding statistics
    * Info
    * Volatility
    * Asset categories
    * Technicals

    Each of these data points is provided in the form of pandas DataFrames and Series.
    """


class TabularRealEstateETFData(_OthersExposureMixin, _BaseTabularETF):
    """Tabular data for real estate ETFs.

    This class provides access to the following real estate ETF exposure data:

    * Asset allocation
    * Country breakdown
    * Market cap breakdown
    * Region breakdown
    * Sector breakdown

    Each of these exposure data points is represented as a pandas Series object.
    """


class TabularMultiAssetETFData(_OthersExposureMixin, _BaseTabularETF):
    """Tabular data for multi-asset ETFs.

    This class provides access to the following multi-asset ETF exposure data:

    * Asset allocation
    * Country breakdown
    * Market cap breakdown
    * Region breakdown
    * Sector breakdown

    Each of these exposure data points is represented as a pandas Series object.
    """


class TabularEquityETFData(_OthersExposureMixin, _BaseTabularETF):
    """Tabular data for equity ETFs.

    This class provides access to the following equity ETF exposure data:

    * Asset allocation
    * Country breakdown
    * Market cap breakdown
    * Region breakdown
    * Sector breakdown

    Each of these exposure data points is represented as a pandas Series object.
    """


class TabularBondETFData(_BondExposureMixin, _BaseTabularETF):
    """Tabular data for bond ETFs.

    This class provides access to the following bond ETF exposure data:

    * Asset allocation
    * Maturity breakdown
    * Bond sector breakdown

    Each of these exposure data points is represented as a pandas Series object.
    """


_mapping = {
    "Equity": TabularEquityETFData,
    "Alternatives": TabularAlternativesETFData,
    "Bond": TabularBondETFData,
    "Multi-Asset": TabularMultiAssetETFData,
    "Currency": TabularCurrencyETFData,
    "Preferred Stock": TabularPreferredStockETFData,
    "Real Estate": TabularRealEstateETFData,
    "Volatility": TabularVolatilityETFData,
}

TabularETF = Union[
    TabularRealEstateETFData,
    TabularBondETFData,
    TabularVolatilityETFData,
    TabularEquityETFData,
    TabularAlternativesETFData,
    TabularCurrencyETFData,
    TabularPreferredStockETFData,
]


def etf_to_tabular_wrapper(
    etf,
) -> TabularETF:
    """Returns a tabular ETF wrapper object for the given ETF object.

    Args:
        etf: An ETF object.

    Returns:
        A tabular ETF wrapper object for the given ETF object.

    Raises:
        ValueError: If the ETF's asset class is not supported.
    """

    cls = _mapping.get(etf.asset_class)
    if cls is None:
        raise ValueError(f"Unsupported asset class: {etf.asset_class}")
    return cls(etf)


__all__ = ["etf_to_tabular_wrapper", "TabularETF"]
