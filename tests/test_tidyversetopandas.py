from tidyversetopandas import tidyversetopandas
import pandas as pd
import pytest

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


def test_select_single_column():
    """Test select function with a single column"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = tidyversetopandas.select(df, "a")
    assert list(result.columns) == ["a"]
    assert result["a"].tolist() == [1, 2, 3]


def test_select_multiple_columns():
    """Test select function with multiple columns"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    result = tidyversetopandas.select(df, "a", "c")
    assert list(result.columns) == ["a", "c"]
    assert result["a"].tolist() == [1, 2, 3]
    assert result["c"].tolist() == [7, 8, 9]


def test_select_non_existing_column():
    """Test select function with a non-existing column"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    with pytest.raises(Exception):
        tidyversetopandas.select(df, "non_existing_column")


def test_select_no_columns():
    """Test select function with no columns specified"""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = tidyversetopandas.select(df)
    assert result.empty
    assert len(result.columns) == 0
    