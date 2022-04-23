'''
Testing & Logging exercise solution

author: Josh
date: March 27, 2021
'''

import logging
logging.basicConfig(
    filename='./test_results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        assert denominator != 0
        assert isinstance(numerator, float)
        assert isinstance(denominator, float)
        fraction_val = numerator / denominator
        logging.info("Testing divide_vals: SUCCESS")
        return fraction_val
    except AssertionError:
        logging.error(
            "Testing divide_vals: The type needs to be float and denominator cannot be 0.")



def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        assert isinstance(text, str)
        total_words = len(text.split())
        logging.info("Testing num_words: SUCCESS")
        return total_words
    except AssertionError:
        logging.error("Testing num_words: The type needs to be a string")


if __name__ == "__main__":
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    num_words(5)
    num_words('This is the best string')
    num_words('one')
