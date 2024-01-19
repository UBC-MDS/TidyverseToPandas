from tidyversetopandas import tidyversetopandas
import pandas as pd
import pytest

@pytest.fixture
def input_df_2():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": ["a", "b", "c"]})
    return df

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
