#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())    # the user input, 2 for first case
    i = 11              # the number of lines

    for number in range(i) :
        if number == 0 :
            continue
        print(n, "x", number, "=", (n * number))