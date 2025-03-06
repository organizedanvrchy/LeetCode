import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    dataframe_list = [df1, df2]
    return pd.concat(dataframe_list)
