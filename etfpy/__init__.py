import pandas as pd

from etfpy.client.etf_client import get_available_etfs_list
from etfpy.etf import ETF, load_etf

pd.options.display.float_format = "{:.2f}".format
