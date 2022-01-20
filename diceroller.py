from random import *
from collections import defaultdict


def roll():
    dice = random()
    return dice


def roll_dice(n):
    '''list the results of rolls'''
    x = defaultdict(
        int)  # provides a default value for the key that does not exists.
    for i in range(n):
        result = roll()
        x[result] += 1  # accumulate results

    print("RESULTS")
# printing results
# returns a new list in ascending order
    for key, value in sorted(x.items()):
        percent = float(value)/n*100
        print('{0:2d}:{1:4d}:({2:.2f}%)'.format(key, value, percent,))


roll_dice(1000)
