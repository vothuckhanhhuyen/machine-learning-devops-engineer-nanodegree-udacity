def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        fraction_val = numerator/denominator
        return fraction_val
    except ZeroDivisionError:
        return "denominator cannot be zero"


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        num_words = len(text.split())
        return num_words
    except AttributeError:
        return "text argument must be a string"
