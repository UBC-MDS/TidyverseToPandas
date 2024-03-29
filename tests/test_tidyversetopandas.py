from tidyversetopandas import tidyversetopandas as ttp
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


@pytest.fixture
def input_df_3():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    return df


def test_mutate_no_func(input_df_1):
    """Test mutate function without a function"""
    df = ttp.mutate(input_df_1, "new_b=7")
    assert df["new_b"].tolist() == [7, 7, 7]


def test_mutate_same_col(input_df_1):
    """Test mutate function that overwrites existing column"""
    df = ttp.mutate(input_df_1, "b = b * 2")
    assert df["b"].tolist() == [8, 10, 12]


def test_mutate_new_col(input_df_1):
    """Test mutate function that creates new column"""
    df = ttp.mutate(input_df_1, "c = a + b")
    assert df["c"].tolist() == [5, 7, 9]


def test_mutate_df_type_error():
    """Test mutate function that raise error for type dataframe"""
    with pytest.raises(TypeError):
        _ = ttp.mutate("abc", "new_b=7")


def test_mutate_expr_type_error(input_df_1):
    """Test mutate function that raise error for type expression"""
    with pytest.raises(ValueError):
        _ = ttp.mutate(input_df_1, 7)


def test_mutate_wrong_expression_error(input_df_1):
    """Test mutate function that raise error for no column specified"""
    with pytest.raises(ValueError):
        _ = ttp.mutate(input_df_1, "asdasd")


def test_arrange_return_df(input_df_2):
    """Test the output is a pandas.DataFrame object"""
    df_sorted = ttp.arrange(input_df_2, True, "A", "C")
    assert isinstance(df_sorted, pd.DataFrame)


def test_arrange_ascend(input_df_2):
    """Test the output is in the ascending order"""
    df_sorted = ttp.arrange(input_df_2, True, "A", "C")

    for i in range(df_sorted.shape[0] - 1):
        assert df_sorted.iloc[i]["A"] <= df_sorted.iloc[i + 1]["A"]


def test_arrange_descend(input_df_2):
    """Test the output is in the descending order"""
    df_sorted = ttp.arrange(input_df_2, False, "A", "C")

    for i in range(df_sorted.shape[0] - 1):
        assert df_sorted.iloc[i]["A"] >= df_sorted.iloc[i + 1]["A"]


def test_arrange_key_error(input_df_2):
    """Test arrange function returns KeyError when input column name does not exist"""
    with pytest.raises(KeyError):
        _ = ttp.arrange(input_df_2, False, "d", "e")


def test_arrange_column_type_error(input_df_2):
    """Test arrange function returns KeyError when input column name is not of str type"""
    with pytest.raises(TypeError):
        _ = ttp.arrange(input_df_2, False, ["a", "b"], 3)

def test_arrange_dataframe_type_error():
    """Test arrange function with a non-DataFrame input"""
    with pytest.raises(TypeError):
        non_df = "This is not a DataFrame"
        _ = ttp.arrange(non_df, "a")


def test_select_single_column(input_df_3):
    """Test select function with a single column"""
    result = ttp.select(input_df_3, "a")
    assert list(result.columns) == ["a"]
    assert result["a"].tolist() == [1, 2, 3]


def test_select_multiple_columns(input_df_3):
    """Test select function with multiple columns"""
    result = ttp.select(input_df_3, "a", "c")
    assert list(result.columns) == ["a", "c"]
    assert result["a"].tolist() == [1, 2, 3]
    assert result["c"].tolist() == [7, 8, 9]


def test_select_non_existing_column(input_df_3):
    """Test select function with a non-existing column"""
    with pytest.raises(Exception):
        ttp.select(input_df_3, "non_existing_column")


def test_select_no_columns(input_df_3):
    """Test select function with no columns specified"""
    with pytest.raises(Exception):
        ttp.select(input_df_3)


def test_select_type_error():
    """Test select function with a non-DataFrame input"""
    with pytest.raises(TypeError):
        non_df = "This is not a DataFrame"
        ttp.select(non_df, "a")


def test_filter_filter_row(input_df_2):
    """Test filter function that filter rows"""
    df = ttp.filter(input_df_2, "A > 1")

    assert df["A"].tolist() == [2, 3]
    assert df["B"].tolist() == [5, 6]
    assert df["C"].tolist() == ["b", "c"]


def test_filter_complex_filter_row(input_df_2):
    """Test filter function that filter rows"""
    df = ttp.filter(input_df_2, "A > 1 and B < 6")

    assert df["A"].tolist() == [2]
    assert df["B"].tolist() == [5]
    assert df["C"].tolist() == ["b"]


def test_filter_df_error():
    """Test filter function that raise error for type dataframe"""
    with pytest.raises(TypeError):
        _ = ttp.filter("abc", "A > 1")


def test_filter_query_error(input_df_2):
    """Test filter function that raise error for type query"""
    with pytest.raises(TypeError):
        _ = ttp.filter(input_df_2, pd.DataFrame([]))
