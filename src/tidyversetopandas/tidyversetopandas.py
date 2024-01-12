import pandas as pd

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
        filter(df, 'column1 > 1')
    """
    return df.query(query)


def arrange(df: pd.DataFrame, ascending: bool = True, *col_name:str):
    """
    Sort a Pandas dataframe in the ascending order

    This function takes a Pandas dataframe and names of the columns, according to which the dataframe is sorted ascendingly/descendingly

    Parameters:
    - df(pandas.DataFrame): The input dataframe object.
    - *col_name(string)

    Returns:
    -------
    pd.DataFrame
        The sorted pandas dataframe with the values in the specified column increasing from the first row to the end of the dataframe

    Example:
    >>> df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
    >>> df_sorted = arrange(df, 'a', 'c')
    """

    return df.sort_values(by=list(col_name), ascending = ascending)
    
