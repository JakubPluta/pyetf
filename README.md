# etfpy

etfpy is a Python library for dealing with extraction ETF data from etfdb.com.

## Installation

* Install with pip as a package [pip](https://pypi.org/project/etfpy)
```
pip install etfpy
```

```
from etfpy import ETF, load_etf
```


* Clone repostiory
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
source env/Scripts/activate
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
from etfpy import ETF, load_etf, get_available_etfs_list
import pprint
# returns list of available ETFs.
etfs = get_available_etfs_list()

# load etf
vwo = load_etf('VWO')
spy = ETF("SPY")
```

```python
# get basic ETF information
pprint.pprint(vwo.info)
```
    {
         '52 Week Hi': '$55.78',
         '52 Week Lo': '$47.65',
         'AUM': '$80,421.8 M',
         'Asset Class': 'Equity',
         'Asset Class Size': 'Large-Cap',
         'Asset Class Style': 'Blend',
         'Brand': 'https://etfdb.com/issuer/vanguard/',
         'Category': 'Size and Style',
         'Category:': 'Emerging Markets Equities',
         'Change:': '$0.25 (-0.0%)',
         'ETF Home Page': 'https://advisors.vanguard.com/investments/products/bnd/vanguard-total-bond-market-etf',
         'Expense Ratio': '0.10%',
         'Focus': 'Total Market',
         'Inception': 'Mar 04, 2005',
         'Index Tracked': 'https://etfdb.com/index/ftse-custom-emerging-markets-all-cap-china-a-inclusion-net-tax-us-ric-index/',
         'Issuer': 'https://etfdb.com/issuer/vanguard/',
         'Last Updated:': 'Dec 09, 2021',
         'Niche': 'Broad-based',
         'P/E Ratio': '7.00',
         'Price:': '$50.14',
         'Region (General)': 'Emerging Markets',
         'Region (Specific)': 'Broad',
         'Segment': 'Equity: Emerging Markets  -  Total Market',
         'Shares': '1,603.3 M',
         'Strategy': 'Vanilla',
         'Structure': 'ETF',
         'Weighting Scheme': 'Market Cap'
     }

```python
# technical analysis metrics
import pprint

pprint.pprint(vwo.technicals)
```

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

```python
# additional script to scrape all etfs from etfdb
from etfpy.client.etfdb_scraper import get_all_etfs

etfs = get_all_etfs(page_size=250)

```


## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
