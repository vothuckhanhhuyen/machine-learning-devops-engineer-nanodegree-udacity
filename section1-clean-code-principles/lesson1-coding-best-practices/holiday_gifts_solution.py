'''
A module to hold the compute_total_price function

Author: Josh
Date: March 21, 2021
'''

import time
import numpy as np


def compute_total_price(pth):
    '''
    prints the total_price and how long it takes to calculate

    INPUTS:
        pth: (string) path of the gifts_cost.txt

    OUTPUTS:
        total_price: (float) total_price of gifts under 25 dollars + tax
    '''
    with open(pth) as file_path:
        gift_costs = file_path.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    start = time.time()
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    print(total_price)
    print('Duration: {} seconds'.format(time.time() - start))

    return total_price


if __name__ == "__main__":
    TOTAL_PRICE_RESULT = compute_total_price('gift_costs.txt')
