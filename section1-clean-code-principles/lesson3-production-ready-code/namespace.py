# conftest.py
import pytest
import logging
from import_df import import_data

def df_plugin():
  return None

# Creating a Dataframe object 'pytest.df' in Namespace
def pytest_configure():
  pytest.df = df_plugin()

# Test function
# See the `pytest.df = df` statement to store the variable in Namespace
def test_import_data():
    try:
        df = import_data("./data/bank_data.csv")
    except FileNotFoundError as err:
        logging.error("File not found")
        raise err
    '''
    Some assertion statements per your requirement.
    '''
    pytest.df = df
    return df

# Test function
# See the `df = pytest.df` statement accessing the Dataframe object from Namespace
def test_function_two():
    df = pytest.df
    '''
    Some assertion statements per your requirement.
    '''