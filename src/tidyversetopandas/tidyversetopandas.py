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
