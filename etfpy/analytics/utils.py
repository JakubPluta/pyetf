from typing import Union, Optional

import numpy as np
import pandas as pd

from etfpy.log import get_logger

logger = get_logger(__name__)


def replace_value_in_df_cell(
    col: pd.Series, to_replace: str, value: str, as_type: type = None
):
    try:
        new_col = col.str.replace(to_replace, value)
    except AttributeError as ae:
        logger.warning("error: %s", str(ae))
        return col

    try:
        if as_type:
            return new_col.astype(as_type)
    except (AttributeError, TypeError) as ate:
        logger.warning("couldn't convert pandas column to type: %s", str(as_type))
        logger.debug("error: %s", str(ate))
    return new_col


def remove_sign_from_values_and_add_as_metric_suffix(
    df, col1="metric", col2="value", to_replace: Union[list, str] = "$"
):
    to_replace = to_replace if isinstance(to_replace, (list, tuple)) else [to_replace]

    for tr in to_replace:
        try:
            rgx = rf"\{tr}"

            df[col1] = np.where(
                df[col2].str.contains(rgx), df[col1] + f" ({tr})", df[col1]
            )
            df[col2] = replace_value_in_df_cell(df[col2], tr, "")
        except Exception as e:
            logger.warning(str(e))
    return df


def clean_data_values_to_float(val: str, round_to=2) -> Optional[float]:
    if val is None:
        return None
    try:
        val = val.replace(",", "")
    except AttributeError as e:
        logger.warning(str(e))

    if val.endswith("%"):
        value = float(val[:-1]) / 100.0
    elif val.endswith("B"):
        value = float(val[:-1]) * 1_000_000_000
    elif val.endswith("M"):
        value = float(val[:-1]) * 1_000_000
    elif val.endswith("K"):
        value = float(val[:-1]) * 1000
    else:
        value = float(val)
    return round(value, round_to)
