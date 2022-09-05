import logging
from import_df import import_data

# Test function 
# It uses the built-in request fixture
def test_import_data(request):
    try:
        df = import_data("./data/bank_data.csv")
    except FileNotFoundError as err:
        logging.error("File not found")
        raise err
    '''
    Some assertion statements per your requirement.
    '''

    request.config.cache.set('cache_df', df)
    return df

# Test function 
# It uses the built-in request fixture
def test_import_data(request):
    try:
        df = import_data("./data/bank_data.csv")
    except FileNotFoundError as err:
        logging.error("File not found")
        raise err
    '''
    Some assertion statements per your requirement.
    '''

    request.config.cache.set('cache_df', df)
    return df