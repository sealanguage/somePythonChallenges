#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tip = round(tip, 1)
    tax = meal_cost * (tax_percent/100)
    tax = round(tax, 2)
    # print(meal_cost, tip_percent, tax_percent)
    # print(tip, tax)

    total_cost = round_down(meal_cost + tip + tax)
    # round_down(total_cost)
    print(total_cost)


    


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)