from tidyversetopandas import tidyversetopandas
import pandas as pd
import pytest
<<<<<<< HEAD
=======

>>>>>>> main

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


<<<<<<< HEAD
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
    
=======
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
>>>>>>> main
