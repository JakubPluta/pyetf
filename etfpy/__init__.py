import pandas as pd

from etfpy.client.etf_client import get_available_etfs_list
from etfpy.etf import ETF, load_etf, load_etf_as_tabular, etfs_to_json

pd.options.display.float_format = "{:.2f}".format
pd.set_option("display.max_columns", None)
