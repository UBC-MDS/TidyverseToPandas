from tidyversetopandas import tidyversetopandas
import pandas as pd
import pytest


@pytest.fixture
def input_df_1():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    return df


@pytest.fixture
def input_df_2():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": ["a", "b", "c"]})
    return df


def test_mutate_no_func(input_df_1):
    """Test mutate function without a function"""
    df = tidyversetopandas.mutate(input_df_1, new_b=7)
    assert df["new_b"].tolist() == [7, 7, 7]


def test_mutate_same_col(input_df_1):
    """Test mutate function that overwrites existing column"""
    df = tidyversetopandas.mutate(input_df_1, b=lambda x: x["b"] * 2)
    assert df["b"].tolist() == [8, 10, 12]


def test_mutate_new_col(input_df_1):
    """Test mutate function that creates new column"""
    df = tidyversetopandas.mutate(input_df_1, c=lambda x: x["a"] + x["b"])
    assert df["c"].tolist() == [5, 7, 9]


def test_filter_filter_row(input_df_2):
    """Test filter function that filter rows"""
    df = tidyversetopandas.filter(input_df_2, "A > 1")

    assert df["A"].tolist() == [2, 3]
    assert df["B"].tolist() == [5, 6]
    assert df["C"].tolist() == ["b", "c"]


def test_filter_complex_filter_row(input_df_2):
    """Test filter function that filter rows"""
    df = tidyversetopandas.filter(input_df_2, "A > 1 and B < 6")

    assert df["A"].tolist() == [2]
    assert df["B"].tolist() == [5]
    assert df["C"].tolist() == ["b"]


def test_filter_df_error():
    """Test filter function that raise error for type dataframe"""
    with pytest.raises(TypeError):
        _ = tidyversetopandas.filter("abc", "A > 1")


def test_filter_query_error(input_df_2):
    """Test filter function that raise error for type query"""
    with pytest.raises(TypeError):
        _ = tidyversetopandas.filter(input_df_2, pd.DataFrame([]))
