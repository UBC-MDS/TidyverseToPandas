from tidyversetopandas import tidyversetopandas
import pandas as pd

def select(dataframe, *columns):
    """
    Select specific columns from a pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to select columns from.
    columns (list of str): Column names to select.

    Returns:
    pdf.DataFrame: A DataFrame with only the selected columns.

    Example DataFrame:
    >>> data = {"column1': [1, 2, 3], 'column2': [4, 5, 6], 'column3': [7, 8, 9]}
    >>> df = pd.DataFrame(data)
    """
    return dataframe[list(columns)]