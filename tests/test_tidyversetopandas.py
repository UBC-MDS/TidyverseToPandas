from tidyversetopandas import tidyversetopandas
import pandas as pd
import unittest
import pytest

@pytest.fixture
def input_df_2():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": ["a", "b", "c"]})
    return df

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

def test_arrange_return_df(input_df_2):
    """Test the output is a pandas.DataFrame object"""
    df_sorted = tidyversetopandas.arrange(input_df_2, True, 'A', 'C')
    assert isinstance(df_sorted, pd.DataFrame)

def test_arrange_ascend(input_df_2):
    """Test the output is in the ascending order"""
    df_sorted = tidyversetopandas.arrange(input_df_2, True, 'A', 'C')

    for i in range(df_sorted.shape[0]-1):
        assert df_sorted.iloc[i]['A'] <= df_sorted.iloc[i+1]['A']

def test_arrange_descend(input_df_2):
    """Test the output is in the descending order"""
    df_sorted = tidyversetopandas.arrange(input_df_2, False, 'A', 'C')

    for i in range(df_sorted.shape[0]-1):
        assert df_sorted.iloc[i]['A'] >= df_sorted.iloc[i+1]['A']

def test_arrange_key_error(input_df_2):
    """Test arrange function returns KeyError when input column name does not exist"""
    with pytest.raises(KeyError):
        _ = tidyversetopandas.arrange(input_df_2, False, 'd', 'e')

def test_arrange_type_error(input_df_2):
    """Test arrange function returns KeyError when input column name does not exist"""
    with pytest.raises(TypeError):
        _ = tidyversetopandas.arrange(input_df_2, False, ['a', 'b'], 3)

           