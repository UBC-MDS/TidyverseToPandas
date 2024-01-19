import pandas as pd


def mutate(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
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
    mutated_df = ttp.mutate(df, new_column = lambda x: x['existing_column'] * 2)
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input 'df' should be a pandas DataFrame.")
    if not kwargs:
        raise ValueError("At least one column must be specified.")

    for col_name, col_value in kwargs.items():
        if callable(col_value):
            df[col_name] = col_value(df)
        else:
            df[col_name] = col_value
    return df


def select(dataframe, *columns):
    """
    Select specific columns from a pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to select columns from.
    columns (list of str): Column names to select.

    Returns:
    pd.DataFrame: A DataFrame with only the selected columns.

    Raises:
    TypeError: If the input dataframe is not a pandas DataFrame.
    ValueError: If any of the specified columns are not in the dataframe.

    Example DataFrame:
    >>> data = {'column1': [1, 2, 3], 'column2': [4, 5, 6], 'column3': [7, 8, 9]}
    >>> df = pd.DataFrame(data)
    >>> ttp.select(df, "column1", "column2")
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The input 'dataframe' should be a pandas DataFrame.")

    if not columns:
        raise ValueError("At least one column must be specified.")

    for col in columns:
        if col not in dataframe.columns:
            raise ValueError(f"Column '{col}' not found in the DataFrame.")

    return dataframe[list(columns)]


def filter(df, query):
    """
    Filter rows in a pandas DataFrame based on a specified query string.

    Parameters:
    df (pd.DataFrame): The DataFrame to filter rows from.
    query (str): A string representing the condition to filter by, similar to a SQL WHERE clause.

    Returns:
    pd.DataFrame: A DataFrame containing only the rows that meet the condition specified in the query string.

    Example:
        data = {'column1': [1, 2, 3], 'column2': [4, 5, 6], 'column3': [7, 8, 9]}
        df = pd.DataFrame(data)
        ttp.filter(df, 'column1 > 1')
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df expect type of pd.DataFrame, got %s" % type(df).__name__)
    if not isinstance(query, str):
        raise TypeError("query expect type of string, got %s" % type(query).__name__)

    return df.query(query)


def arrange(df: pd.DataFrame, ascending: bool = True, *col_name: str):
    """
    Sort a Pandas dataframe in the ascending order

    This function takes a Pandas dataframe and names of the columns, according to which the dataframe is sorted ascendingly/descendingly

    Parameters:
    df(pandas.DataFrame): The input dataframe object.
    *col_name(string)

    Returns:
    -------
    pd.DataFrame
        The sorted pandas dataframe with the values in the specified column increasing from the first row to the end of the dataframe

    Example:
    >>> df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
    >>> df_sorted = ttp.arrange(df, True, 'a', 'c')
    """
    try:
        if any(not isinstance(c, str) for c in col_name):
            raise TypeError("All column names must be of string type!")
        sorted = df.sort_values(by=list(col_name), ascending=ascending)

    except KeyError:
        raise KeyError("Column(s) does not exist in the provided dataframe!")
    return sorted
