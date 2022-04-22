# your task is to clean this script in
# a way that uses the code as a single function
# that takes a path and returns the total_price variable
# that meets pep8 standards and receives a 10 score using pylint

# You may need to:
# pip install autopep8
# pip install pylint

import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')

gift_costs = np.array(gift_costs).astype(int)  # convert string to int

start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

start = time.time()

total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))
