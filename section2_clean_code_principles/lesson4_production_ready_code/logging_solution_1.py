'''
Logging exercise solution

author: Josh
date: March 27, 2021
'''
import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def sum_vals(first_val, second_val):
    '''
    Args:
        first_val: (int)
        second_val: (int)
    Return:
        first_val + second_val (int)
    '''
    try:
        check_val = first_val + 1
        print("check_val type: {}".format(check_val))
        logging.info("Summing first_val + second_val: SUCCESS")
        return first_val + second_val
    except TypeError:
        logging.error("first_val and second_val should be integers.")

if __name__ == "__main__":
    sum_vals(4, 5)
    sum_vals('no', 'way')
