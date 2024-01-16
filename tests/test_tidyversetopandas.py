from tidyversetopandas import tidyversetopandas
import pandas as pd


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
