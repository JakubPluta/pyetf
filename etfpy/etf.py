from etfpy.analytics.tabular_etf import TabularETF, etf_to_tabular_wrapper
from etfpy.client.etf_client import ETFDBClient as _ETFDBClient
from etfpy.utils import get_class_property_methods


class ETF(_ETFDBClient):
    """ETF Client

    Main class to interact with ETFDB data.
    Under the hood when instantiated it scrapes the data for given ETF symbol e.g SPY,
    and parse all the data for every section.
    You can access everything with ETF class properties e.g info, holdings ...

    """

    def __init__(self, ticker: str) -> None:
        """Initialize ETF class"""
        super().__init__(ticker)

    @property
    def info(self) -> dict:
        """Gets basic information about ETF.

        Example:
        ---------------
        >>> etf = ETF("SPY")
        >>> etf.info
        {'52 Week Hi': '$457.83',
         '52 Week Lo': '$342.72',
         'AUM': '$402,034.0 M',
         'Asset Class': 'Equity',
         'Asset Class Size': 'Large-Cap',
         'Asset Class Style': 'Blend',
         'Brand': 'https://etfdb.com/issuer/spdr/',
         'Category': 'Size and Style',
         'Category:': 'Large Cap Growth Equities',
         'Change:': '$1.04 (-0.0%)',
         'ETF Home Page': 'https://www.spdrs.com/product/fund.seam?ticker=SPY',
         'Expense Ratio': '0.09%',
         'Focus': 'Large Cap',
         'Inception': 'Jan 22, 1993',
         'Index Tracked': 'https://etfdb.com/index/sp-500-index/',
         'Issuer': 'https://etfdb.com/issuer/state-street/',
         'Last Updated:': 'Sep 30, 2023',
         'Niche': 'Broad-based',
         'P/E Ratio': {'ETF Database Category Average': '15.15',
                       'FactSet Segment Average': '5.84',
                       'SPY': '17.86'},
         'Price:': '$427.48',
         'Region (General)': 'North America',
         'Region (Specific)': 'U.S.',
         'Segment': 'Equity: U.S.  -  Large Cap',
         'Shares': '938.3 M',
         'Strategy': 'Vanilla',
         'Structure': 'UIT',
         'Symbol': 'SPY',
         'Url': 'https://etfdb.com/etf/SPY',
         'Weighting Scheme': 'Market Cap'}
        """
        return self._basic_info()

    @property
    def holdings(self) -> list:
        """Gets basic information about ETF.

        Example:
        ---------------
        >>> etf = ETF("SPY")
        >>> etf.holdings

         [{'Holding': 'Apple Inc.',
               'Share': '7.19%',
               'Symbol': 'AAPL',
               'Url': '/stock/AAPL/'},
              {'Holding': 'Microsoft Corporation',
               'Share': '6.51%',
               'Symbol': 'MSFT',
               'Url': '/stock/MSFT/'},
              {'Holding': 'Amazon.com, Inc.',
               'Share': '3.33%',
               'Symbol': 'AMZN',
               'Url': '/stock/AMZN/'},
              {'Holding': 'NVIDIA Corporation',
               'Share': '2.95%',
               'Symbol': 'NVDA',
               'Url': '/stock/NVDA/'},
              {'Holding': 'Alphabet Inc. Class A',
               'Share': '2.03%',
               'Symbol': 'GOOGL',
               'Url': '/stock/GOOGL/'},
              {'Holding': 'Meta Platforms Inc. Class A',
               'Share': '1.84%',
               'Symbol': 'META',
               'Url': '/stock/META/'},
              {'Holding': 'Tesla, Inc.',
               'Share': '1.83%',
               'Symbol': 'TSLA',
               'Url': '/stock/TSLA/'},
              {'Holding': 'Alphabet Inc. Class C',
               'Share': '1.76%',
               'Symbol': 'GOOG',
               'Url': '/stock/GOOG/'},
              {'Holding': 'Berkshire Hathaway Inc. Class B',
               'Share': '1.67%',
               'Symbol': 'BRK.B',
               'Url': '/stock/BRK.B/'},
              {'Holding': 'UnitedHealth Group Incorporated',
               'Share': '1.25%',
               'Symbol': 'UNH',
               'Url': '/stock/UNH/'},
              {'Holding': 'JPMorgan Chase & Co.',
               'Share': '1.22%',
               'Symbol': 'JPM',
               'Url': '/stock/JPM/'},
              {'Holding': 'Johnson & Johnson',
               'Share': '1.17%',
               'Symbol': 'JNJ',
               'Url': '/stock/JNJ/'},
              {'Holding': 'Exxon Mobil Corporation',
               'Share': '1.16%',
               'Symbol': 'XOM',
               'Url': '/stock/XOM/'},
              {'Holding': 'Visa Inc. Class A',
               'Share': '1.03%',
               'Symbol': 'V',
               'Url': '/stock/V/'},
              {'Holding': 'Broadcom Inc.',
               'Share': '0.98%',
               'Symbol': 'AVGO',
               'Url': '/stock/AVGO/'}
               ],
        """
        return self._holdings()

    @property
    def asset_categories(self) -> dict:
        return self._asset_categories()

    @property
    def holding_statistics(self):
        return self._number_of_holdings()

    @property
    def exposure(self) -> dict:
        """Get ETF exposure information.

        Example:
        ---------------
        >>> etf = ETF("SPY")
        >>> etf.exposure
        {
        'Asset Allocation': {'CASH': 0.3, 'Share/Common/Ordinary': 99.7},
        'Country Breakdown': {'Bermuda': 0.13,
                       'Ireland': 1.64,
                       'Israel': 0.02,
                       'Netherlands': 0.14,
                       'Other': 0.3,
                       'Switzerland': 0.39,
                       'United Kingdom': 0.7,
                       'United States': 96.68},
        'Market Cap Breakdown': {'Large': 97.64, 'Micro': 0, 'Mid': 2.06, 'Small': 0},
        'Market Tier Breakdown': {},
        'Region Breakdown': {'North, Central and South America': 99.7, 'Other': 0.3},
        'Sector Breakdown': {'CASH': 0.3,
                      'Commercial Services': 3.01,
                      'Communications': 0.88,
                      'Consumer Durables': 2.58,
                      'Consumer Non-Durables': 4.93,
                      'Consumer Services': 3.54,
                      'Distribution Services': 0.84,
                      'Electronic Technology': 16.89,
                      'Energy Minerals': 3.99,
                      'Finance': 12.2,
                      'Health Services': 2.52,
                      'Health Technology': 10.08,
                      'Industrial Services': 1.07,
                      'Non-Energy Minerals': 0.55,
                      'Process Industries': 2.02,
                      'Producer Manufacturing': 3.58,
                      'Retail Trade': 7.25,
                      'Technology Services': 19.72,
                      'Transportation': 1.6,
                      'Utilities': 2.45}}
        """
        return self._exposure()

    @property
    def volatility(self) -> dict:
        """Get ETF volatility information.

        Example:
        ---------------
        >>> etf = ETF("SPY")
        >>> etf.volatility

        {'20 Day Volatility': '10.61%',
         '200 Day Volatility': '10.91%',
         '5 Day Volatility': '200.37%',
         '50 Day Volatility': '11.16%',
         'Beta': '1.0',
         'Standard Deviation': '26.89%'
         }

        """
        return self._volatility()

    @property
    def technicals(self) -> dict:
        """Get ETF technicals information.

        Example:
        ---------------
        >>> etf = ETF("SPY")
        >>> etf.technicals

        {'20 Day MA': '$439.23',
         '60 Day MA': '$443.62',
         'Average Spread ($)': '1.05',
         'Average Spread (%)': '1.05',
         'Lower Bollinger (10 Day)': '$420.35',
         'Lower Bollinger (20 Day)': '$423.50',
         'Lower Bollinger (30 Day)': '$425.58',
         'MACD 100 Period': '-8.42',
         'MACD 15 Period': '-9.54',
         'Maximum Premium Discount (%)': '0.10',
         'Median Premium Discount (%)': '0.01',
         'RSI 10 Day': '32',
         'RSI 20 Day': '38',
         'RSI 30 Day': '43',
         'Resistance Level 1': '$430.92',
         'Resistance Level 2': '$434.35',
         'Stochastic Oscillator %D (1 Day)': '45.34',
         'Stochastic Oscillator %D (5 Day)': '36.54',
         'Stochastic Oscillator %K (1 Day)': '45.70',
         'Stochastic Oscillator %K (5 Day)': '26.29',
         'Support Level 1': '$424.98',
         'Support Level 2': '$422.47',
         'Tracking Difference Max Downside (%)': '-0.10',
         'Tracking Difference Max Upside (%)': '-0.02',
         'Tracking Difference Median (%)': '-0.03',
         'Ultimate Oscillator': '37',
         'Upper Bollinger (10 Day)': '$445.68',
         'Upper Bollinger (20 Day)': '$455.40',
         'Upper Bollinger (30 Day)': '$454.25',
         'Williams % Range 10 Day': '77.12',
         'Williams % Range 20 Day': '82.58'
         }
        """
        return self._technicals()

    @property
    def performance(self) -> dict:
        """Get ETF performance information.

        Example:
        ---------------
        >>> etf = ETF("SPY")
        >>> etf.performance

        {
        '1 Month Return': {'ETF Database Category Average': '-2.89%',
                    'Factset Segment Average': '-2.07%',
                    'SPY': '-3.11%'},
        '1 Year Return': {'ETF Database Category Average': '19.00%',
                   'Factset Segment Average': '10.82%',
                   'SPY': '19.69%'},
        '3 Month Return': {'ETF Database Category Average': '-2.10%',
                    'Factset Segment Average': '-1.07%',
                    'SPY': '-1.70%'},
        '3 Year Return': {'ETF Database Category Average': '5.55%',
                   'Factset Segment Average': '4.06%',
                   'SPY': '10.18%'},
        '5 Year Return': {'ETF Database Category Average': '5.33%',
                   'Factset Segment Average': '2.06%',
                   'SPY': '9.83%'},
        'YTD Return': {'ETF Database Category Average': '14.37%',
                'Factset Segment Average': '6.70%',
                'SPY': '13.02%'}}
        """
        return self._performance()

    @property
    def dividends(self) -> dict:
        """Get ETF dividends information.

         Example:
         ---------------
         >>> etf = ETF("SPY")
         >>> etf.dividends

        {
        'Annual Dividend Rate': {'ETF Database Category Average': '$ 0.95',
                          'FactSet Segment Average': '$ 0.63',
                          'SPY': '$ 6.51'},
        'Annual Dividend Yield': {'ETF Database Category Average': '1.37%',
                           'FactSet Segment Average': '1.41%',
                           'SPY': '1.52%'},
        'Dividend': {'ETF Database Category Average': '$ 0.33',
                            'FactSet Segment Average': '$ 0.16',
                            'SPY': '$ 1.58'},
        'Dividend Date': {'ETF Database Category Average': 'N/A',
                           'FactSet Segment Average': 'N/A',
                           'SPY': '2023-09-15'}
        }
        """
        return self._dividends()

    def to_dict(self) -> dict:
        """
        Convert the object to a dictionary.

        Returns
        -------
        Dict
            A dictionary containing the object's properties and values.

        """
        data = {}
        method_list = get_class_property_methods(self.__class__)
        for m in method_list:
            if not m.startswith("_"):
                data[m.title()] = getattr(self, m)
        return data

    def to_tabular(self) -> TabularETF:
        """Returns a tabular ETF wrapper object for the given ETF object."""
        return etf_to_tabular_wrapper(self)


def load_etf(etf: str) -> ETF:
    """
    Load an ETF object.

    Parameters
    ----------
    etf : str
        The ticker symbol of the ETF to load.

    Returns
    -------
    ETF
        An ETF object.

    Examples
    --------
    >>> etf = load_etf("SPY")
    """
    return ETF(etf)
