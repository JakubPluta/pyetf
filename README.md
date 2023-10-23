# ETFpy
[![codecov](https://codecov.io/gh/JakubPluta/pyetf/graph/badge.svg?token=736JAQGR1C)](https://codecov.io/gh/JakubPluta/pyetf)
[![PyPI version](https://badge.fury.io/py/etfpy.svg)](https://badge.fury.io/py/etfpy)
<a target="new" href="https://github.com/JakubPluta/pyetf"><img border=0 src="https://img.shields.io/github/stars/JakubPluta/pyetf.svg?style=social&label=Star&maxAge=60" alt="Star this repo"></a>

**ETFpy** is a Python library that allows users to scrape data from etfdb.com, 
a website that provides comprehensive information on ETFs, 
including trading data, performance metrics, assets allocations end more. 

## Installation

### Install with pip as a package [pip](https://pypi.org/project/etfpy)
```
pip install etfpy
```
or

### Clone repostiory
```bash
# clone repository
git clone https://github.com/JakubPluta/pyetf.git
```
```bash
# navigate to cloned project and create virtual environment
python -m venv env
```
```bash
# activate virtual environment
source env/Scripts/activate # or source env/bin/activate
```

```python
# install poetry
pip install poetry
```

```python
# install packages
poetry install
```

## Usage

```python
>>> from etfpy import ETF, load_etf, get_available_etfs_list

# returns list of available ETFs.
>>> etfs = get_available_etfs_list()
>>> etfs
>>> ['SPY', 'IVV', 'VOO', 'VTI', 'QQQ', 'VEA', 'VTV', 'IEFA', 'BND', 'AGG', 'VUG', 'IJH', ... ]

# load etf
>>> vwo = load_etf('VWO')
# or
>>> spy = ETF("SPY")
```

#### Get basic ETF information

```python
>>> spy.info
{
'52 Week Hi': '$457.83',
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
'P/E Ratio': {
    'ETF Database Category Average': '15.15',
    'FactSet Segment Average': '5.84',
    'SPY': '17.86'
 },
'Price:': '$427.48',
'Region (General)': 'North America',
'Region (Specific)': 'U.S.',
'Segment': 'Equity: U.S.  -  Large Cap',
'Shares': '938.3 M',
'Strategy': 'Vanilla',
'Structure': 'UIT',
'Symbol': 'SPY',
'Url': 'https://etfdb.com/etf/SPY',
'Weighting Scheme': 'Market Cap'
}
```

#### Get technical analysis metrics
```python
>>> spy.technicals
{
'20 Day MA': '$50.45',
'60 Day MA': '$50.74',
'Average Spread ($)': '1.00',
'Average Spread (%)': '1.00',
'Lower Bollinger (10 Day)': '$48.64',
'Lower Bollinger (20 Day)': '$48.33',
'Lower Bollinger (30 Day)': '$48.81',
'MACD 100 Period': '-0.74',
'MACD 15 Period': '0.20',
'Maximum Premium Discount (%)': '0.82',
'Median Premium Discount (%)': '0.27',
'RSI 10 Day': '49',
'RSI 20 Day': '47',
'RSI 30 Day': '47',
'Resistance Level 1': 'n/a',
'Resistance Level 2': '$50.53',
'Stochastic Oscillator %D (1 Day)': '53.54',
'Stochastic Oscillator %D (5 Day)': '73.08',
'Stochastic Oscillator %K (1 Day)': '55.09',
'Stochastic Oscillator %K (5 Day)': '57.68',
'Support Level 1': 'n/a',
'Support Level 2': '$49.86',
'Tracking Difference Max Downside (%)': '-0.87',
'Tracking Difference Max Upside (%)': '0.16',
'Tracking Difference Median (%)': '-0.36',
'Ultimate Oscillator': '47',
'Upper Bollinger (10 Day)': '$50.47',
'Upper Bollinger (20 Day)': '$52.61',
'Upper Bollinger (30 Day)': '$52.50',
'Williams % Range 10 Day': '19.32',
'Williams % Range 20 Day': '59.31'
}
```
#### Get dividends metrics
```python
>>> spy.dividends
>>> {
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
```

#### Get performance metrics
```python
>>> spy.performance
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
        'SPY': '13.02%'}
}
```


#### Get volatility metrics

```python
>>> spy.volatility
{
     '20 Day Volatility': '10.61%',
     '200 Day Volatility': '10.91%',
     '5 Day Volatility': '200.37%',
     '50 Day Volatility': '11.16%',
     'Beta': '1.0',
     'Standard Deviation': '26.89%'
}
```

#### Get holding statistics
```python
>>> spy.holding_statistics
{
'% of Assets in Top 10': {'ETF Database Category Average': '42.67%',
                       'FactSet Segment Average': '59.61%',
                       'SPY': '39.52%'},
'% of Assets in Top 15': {'ETF Database Category Average': '51.39%',
                       'FactSet Segment Average': '64.18%',
                       'SPY': '49.25%'},
'% of Assets in Top 50': {'ETF Database Category Average': '80.70%',
                       'FactSet Segment Average': '80.85%',
                       'SPY': '83.04%'},
'Number of Holdings': {'ETF Database Category Average': '412',
                    'FactSet Segment Average': '174',
                    'SPY': '1000'}
}
```
#### Get holdings
```python
>>> spy.holdings

[{'Holding': 'Apple Inc.',
  'Share': '7.19%',
  'Symbol': 'AAPL',
  'Url': 'https://etfdb.com/stock/AAPL/'},
 {'Holding': 'Microsoft Corporation',
  'Share': '6.51%',
  'Symbol': 'MSFT',
  'Url': 'https://etfdb.com/stock/MSFT/'},
 {'Holding': 'Amazon.com, Inc.',
  'Share': '3.33%',
  'Symbol': 'AMZN',
  'Url': 'https://etfdb.com/stock/AMZN/'},
 {'Holding': 'NVIDIA Corporation',
  'Share': '2.95%',
  'Symbol': 'NVDA',
  'Url': 'https://etfdb.com/stock/NVDA/'},
 {'Holding': 'Alphabet Inc. Class A',
  'Share': '2.03%',
  'Symbol': 'GOOGL',
  'Url': 'https://etfdb.com/stock/GOOGL/'},
 {'Holding': 'Meta Platforms Inc. Class A',
  'Share': '1.84%',
  'Symbol': 'META',
  'Url': 'https://etfdb.com/stock/META/'},
 {'Holding': 'Tesla, Inc.',
  'Share': '1.83%',
  'Symbol': 'TSLA',
  'Url': 'https://etfdb.com/stock/TSLA/'},
 {'Holding': 'Alphabet Inc. Class C',
  'Share': '1.76%',
  'Symbol': 'GOOG',
  'Url': 'https://etfdb.com/stock/GOOG/'},
 {'Holding': 'Berkshire Hathaway Inc. Class B',
  'Share': '1.67%',
  'Symbol': 'BRK.B',
  'Url': 'https://etfdb.com/stock/BRK.B/'},
 {'Holding': 'UnitedHealth Group Incorporated',
  'Share': '1.25%',
  'Symbol': 'UNH',
  'Url': 'https://etfdb.com/stock/UNH/'},
 {'Holding': 'JPMorgan Chase & Co.',
  'Share': '1.22%',
  'Symbol': 'JPM',
  'Url': 'https://etfdb.com/stock/JPM/'},
 {'Holding': 'Johnson & Johnson',
  'Share': '1.17%',
  'Symbol': 'JNJ',
  'Url': 'https://etfdb.com/stock/JNJ/'},
 {'Holding': 'Exxon Mobil Corporation',
  'Share': '1.16%',
  'Symbol': 'XOM',
  'Url': 'https://etfdb.com/stock/XOM/'},
 {'Holding': 'Visa Inc. Class A',
  'Share': '1.03%',
  'Symbol': 'V',
  'Url': 'https://etfdb.com/stock/V/'},
 {'Holding': 'Broadcom Inc.',
  'Share': '0.98%',
  'Symbol': 'AVGO',
  'Url': 'https://etfdb.com/stock/AVGO/'}]


```

#### Get exposures

```python
>>> spy.exposure
{'Asset Allocation': {'CASH': 0.38, 'Share/Common/Ordinary': 99.59},
 'Country Breakdown': {'Bermuda': 0.13,
                       'Ireland': 1.63,
                       'Israel': 0.02,
                       'Netherlands': 0.14,
                       'Other': 0.38,
                       'Switzerland': 0.4,
                       'United Kingdom': 0.69,
                       'United States': 96.58},
 'Market Cap Breakdown': {'Large': 97.42, 'Micro': 0, 'Mid': 2.2, 'Small': 0},
 'Market Tier Breakdown': {},
 'Region Breakdown': {'North, Central and South America': 99.59, 'Other': 0.38},
 'Sector Breakdown': {'CASH': 0.38,
                      'Commercial Services': 3.02,
                      'Communications': 0.84,
                      'Consumer Durables': 2.65,
                      'Consumer Non-Durables': 4.78,
                      'Consumer Services': 3.43,
                      'Distribution Services': 0.92,
                      'Electronic Technology': 17.34,
                      'Energy Minerals': 3.64,
                      'Finance': 11.96,
                      'Health Services': 2.55,
                      'Health Technology': 9.99,
                      'Industrial Services': 1.02,
                      'Non-Energy Minerals': 0.54,
                      'Process Industries': 1.98,
                      'Producer Manufacturing': 3.55,
                      'Retail Trade': 7.19,
                      'Technology Services': 20.34,
                      'Transportation': 1.5,
                      'Utilities': 2.35}
 }
```

#### Get quotes

```python
>>> spy.get_quotes(interval="daily", periods=7)
[{'close': 424.5,
  'date': datetime.date(2023, 10, 5),
  'high': 425.37,
  'low': 421.1701,
  'open': 424.36,
  'symbol': 'SPY',
  'volume': 70142700},
 {'close': 429.54,
  'date': datetime.date(2023, 10, 6),
  'high': 431.125,
  'low': 420.6,
  'open': 421.97,
  'symbol': 'SPY',
  'volume': 113273300},
 {'close': 432.29,
  'date': datetime.date(2023, 10, 9),
  'high': 432.88,
  'low': 427.0101,
  'open': 427.58,
  'symbol': 'SPY',
  'volume': 80374300},
 {'close': 434.54,
  'date': datetime.date(2023, 10, 10),
  'high': 437.22,
  'low': 432.53,
  'open': 432.94,
  'symbol': 'SPY',
  'volume': 78607200},
 {'close': 436.32,
  'date': datetime.date(2023, 10, 11),
  'high': 436.58,
  'low': 433.18,
  'open': 435.64,
  'symbol': 'SPY',
  'volume': 62451700},
 {'close': 433.66,
  'date': datetime.date(2023, 10, 12),
  'high': 437.335,
  'low': 431.23,
  'open': 436.95,
  'symbol': 'SPY',
  'volume': 81154200},
 {'close': 431.5,
  'date': datetime.date(2023, 10, 13),
  'high': 436.45,
  'low': 429.88,
  'open': 435.21,
  'symbol': 'SPY',
  'volume': 95201100}]

```

You can also wrap ETF object with pandas DataFrames, and work with the data in tabular form.
You will have access to mostly the same methods as etf has, but as a result you will see DataFrame or Series.

```python
>>> from etfpy import ETF
>>> spy = ETF("SPY")
>>> spy_tabular = spy.to_tabular()
```
```python
>>> spy.exposure_by_sector
```

| Metric                  | Value       |
|-------------------------|-------------|
| Technology Services     | 20.34       |
| Electronic Technology   | 17.34       |
| Finance                 | 11.96       |
| Health Technology       | 9.99        |
| Retail Trade            | 7.19        |
| Consumer Non-Durables   | 4.78        |
| Energy Minerals         | 3.64        |
| Producer Manufacturing  | 3.55        |
| Consumer Services       | 3.43        |
| Commercial Services     | 3.02        |
| Consumer Durables       | 2.65        |
| Health Services         | 2.55        |
| Utilities               | 2.35        |
| Process Industries      | 1.98        |
| Transportation          | 1.50        |
| Industrial Services     | 1.02        |
| Distribution Services   | 0.92        |
| Communications          | 0.84        |
| Non-Energy Minerals     | 0.54        |
| CASH                    | 0.38        |

```python
>>> spy.info
```
| Metric               | Value                                   |
|----------------------|-----------------------------------------|
| Symbol               | SPY                                     |
| Url                  | https://etfdb.com/etf/SPY               |
| Issuer               | https://etfdb.com/issuer/state-street/  |
| Brand                | https://etfdb.com/issuer/spdr/          |
| Inception            | Jan 22, 1993                            |
| Index Tracked        | https://etfdb.com/index/sp-500-index/   |
| Last Updated         | Oct 11, 2023                            |
| Category             | Size and Style                          |
| Asset Class          | Equity                                  |
| Segment              | Equity: U.S.  -  Large Cap              |
| Focus                | Large Cap                               |
| Niche                | Broad-based                             |
| Strategy             | Vanilla                                 |
| Weighting Scheme     | Market Cap                              |

```python
>>> spy.info_numeric
```


| Metric              | Value           |
|---------------------|-----------------|
| Expense Ratio (%)   | 0.09            |
| Price ($)           | 434.54          |
| Change($)           | 2.25            |
| P/E Ratio           | 17.86           |
| 52 Week Lo ($)      | 342.72          |
| 52 Week Hi ($)      | 457.83          |
| AUM ($)             | 398435000000.00 |
| Shares              | 927600000.00    |

```python
>>> spy.dividends
```

|                               | dividend      | dividend_date    | %_annual_dividend_rate  | annual_dividend_yield  |
|-------------------------------|---------------|------------------|-------------------------|------------------------|
| SPY                           | 1.58          | 2023-09-15       | 6.51                    | 1.51                   |
| ETF Database Category Average | 0.33          | None             | 0.92                    | 1.30                   |
| FactSet Segment Average       | 0.17          | None             | 0.59                    | 1.33                   |

```python
>>> spy.technicals
```

| Metric                                | Value      |
|---------------------------------------|------------|
| 20 Day MA ($)                         | 432.92     |
| 60 Day MA ($)                         | 441.77     |
| MACD 15 Period                        | 5.54       |
| MACD 100 Period                       | -2.65      |
| Williams % Range 10 Day               | 15.73      |
| Williams % Range 20 Day               | 51.02      |
| RSI 10 Day                            | 55         |
| RSI 20 Day                            | 49         |
| RSI 30 Day                            | 49         |
| Ultimate Oscillator                   | 60         |
| Lower Bollinger (10 Day) ($)          | 420.25     |
| Upper Bollinger (10 Day) ($)          | 434.00     |
| Lower Bollinger (20 Day) ($)          | 416.98     |
| Upper Bollinger (20 Day) ($)          | 448.76     |
| Lower Bollinger (30 Day) ($)          | 418.95     |
| Upper Bollinger (30 Day) ($)          | 455.88     |
| Support Level 1 ($)                   | 432.31     |
| Support Level 2 ($)                   | 430.07     |
| Resistance Level 1 ($)                | 437.00     |
| Resistance Level 2 ($)                | 439.45     |
| Stochastic Oscillator %D (1 Day)      | 65.76      |
| Stochastic Oscillator %D (5 Day)      | 72.22      |
| Stochastic Oscillator %K (1 Day)      | 65.64      |
| Stochastic Oscillator %K (5 Day)      | 56.38      |
| Tracking Difference Median (%)        | -0.03      |
| Tracking Difference Max Upside (%)    | -0.02      |
| Tracking Difference Max Downside (%)  | -0.10      |
| Median Premium Discount (%)           | 0.01       |
| Maximum Premium Discount (%)          | 0.10       |
| Average Spread (%)                    | 1.06       |
| Average Spread ($)                    | 1.06       |

```python
>>> spy.get_quotes(interval="daily", periods=365)
```

| Symbol   | Date       | Open     | High     | Low      | Close    | Volume       |
|----------|------------|----------|----------|----------|----------|--------------|
| SPY      | 2022-05-10 | 404.49   | 406.08   | 394.82   | 399.09   | 132497200    |
| SPY      | 2022-05-11 | 398.07   | 404.04   | 391.96   | 392.75   | 142361000    |
| SPY      | 2022-05-12 | 389.37   | 395.80   | 385.15   | 392.34   | 125090700    |
| SPY      | 2022-05-13 | 396.71   | 403.18   | 395.61   | 401.72   | 104174400    |
| SPY      | 2022-05-16 | 399.98   | 403.97   | 397.60   | 400.09   | 78622400     |
| -------- | ------     | -------- | -------- | -------- | -------- | ------------ |
| -------- | ------     | -------- | -------- | -------- | -------- | ------------ |
| SPY      | 2023-10-09 | 427.58   | 432.88   | 427.01   | 432.29   | 80374300     |
| SPY      | 2023-10-10 | 432.94   | 437.22   | 432.53   | 434.54   | 78607200     |
| SPY      | 2023-10-11 | 435.64   | 436.58   | 433.18   | 436.32   | 62451700     |
| SPY      | 2023-10-12 | 436.95   | 437.33   | 431.23   | 433.66   | 81154200     |



If you want to scrape list of all etfs with some basic information in terminal use:
```bash
python etfpy/scripts/scrape_etfs.py
or 
bash jobs/run_scrape_etfs.sh
or
make scrape
```
Output data will be stored in `.\etfpy\data\etfs\etfs_list.json`

Run tests & check coverage 
```bash
# run all tests
make test

# pytest cov
make cov
```

To lint
```bash
make pretty
```


## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
