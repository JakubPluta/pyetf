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
    df, col1="metric", col2="value", to_replace="$"
):
    try:
        rgx = rf"\{to_replace}"

        df[col1] = np.where(
            df[col2].str.contains(rgx), df[col1] + f" ({to_replace})", df[col1]
        )
        df[col2] = replace_value_in_df_cell(df[col2], to_replace, "")
    except Exception as e:
        logger.warning(str(e))
    return df
