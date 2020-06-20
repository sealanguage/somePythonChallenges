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
    tip = round(meal_cost * (tip_percent/100.0))
    tax = meal_cost * (tax_percent/100.0)
    tax = round(tax, 2)

    total_cost = meal_cost + tip + tax
    print(round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
