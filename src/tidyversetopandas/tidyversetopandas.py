import pandas as pd


def pandas_mutate(df, **kwargs):
    """
    Add new columns to a Pandas DataFrame or modify existing ones, similar to dplyr's mutate in R.

    Parameters:
        df (pd.DataFrame): The DataFrame to be mutated.

        **kwargs: Keyword arguments where keys are the new column names and values are
                either a series, a callable (function), or a single value. If a callable is provided,
                it should accept a DataFrame and return a Series.

    Returns:
        pd.DataFrame: The mutated DataFrame with added or modified columns.

    Example:
    mutated_df = pandas_mutate(df, new_column = lambda x: x['existing_column'] * 2)
    """
    for col_name, col_value in kwargs.items():
        if callable(col_value):
            df[col_name] = col_value(df)
        else:
            df[col_name] = col_value
    return df
