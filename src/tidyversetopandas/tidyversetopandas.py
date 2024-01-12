import pandas as pd

def arrange(df: pd.DataFrame, ascending: bool = True, *col_name:str):
    """
    Sort a Pandas dataframe in the ascending order

    This function takes a Pandas dataframe and names of the columns, according to which the dataframe is sorted ascendingly/descendingly

    Parameters:
    -------
    - df(pandas.DataFrame): The input dataframe object.
    - *col_name(string)

    Returns:
    -------
    pd.DataFrame
        The sorted pandas dataframe with the values in the specified column increasing from the first row to the end of the dataframe
    
    Example:
    >>> df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
    >>> df_sorted = tidyversetopandas.arrange(df, 'a', 'c')
    """

    return df.sort_values(by=list(col_name), ascending = ascending)