from tidyversetopandas import tidyversetopandas
import pandas as pd
import unittest

def test_mutate_no_func():
    """Test mutate function without a function"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df = tidyversetopandas.mutate(df, new_b=7)
    assert df["new_b"].tolist() == [7, 7, 7]


def test_mutate_same_col():
    """Test mutate function that overwrites existing column"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df = tidyversetopandas.mutate(df, b=lambda x: x["b"] * 2)
    assert df["b"].tolist() == [8, 10, 12]


def test_mutate_new_col():
    """Test mutate function that creates new column"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df = tidyversetopandas.mutate(df, c=lambda x: x["a"] + x["b"])
    assert df["c"].tolist() == [5, 7, 9]

def test_arrange_return_df():
    """Test the output is a pandas.DataFrame object"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0, 1, 9]})
    df_sorted = tidyversetopandas.arrange(df, True, 'a', 'c')
    assert isinstance(df_sorted, pd.DataFrame)

def test_arrange_ascend():
    """Test the output is in the ascending order"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0, 1, 9]})
    df_sorted = tidyversetopandas.arrange(df, True, 'a', 'c')

    for i in range(df_sorted.shape[0]-1):
        assert df_sorted.iloc[i]['a'] <= df_sorted.iloc[i+1]['a']

def test_arrange_descend():
    """Test the output is in the ascending order"""
    """Test the output is in the ascending order"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0, 1, 9]})
    df_sorted = tidyversetopandas.arrange(df, False, 'a', 'c')

    for i in range(df_sorted.shape[0]-1):
        assert df_sorted.iloc[i]['a'] >= df_sorted.iloc[i+1]['a']

class TestKeyError(unittest.TestCase):
    def test_column_not_found(self):
        with self.assertRaises(KeyError):
            df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0, 1, 9]})
            df_sorted = tidyversetopandas.arrange(df, False, 'd', 'e')
           