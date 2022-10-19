#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length_of_list = len(arr)
    pos_counter = 0
    zero_counter = 0
    neg_counter = 0

    for i in arr:
        if i > 0:
            pos_counter += 1
        elif i < 0:
            neg_counter += 1
        else:
            zero_counter += 1

    print(pos_counter / length_of_list)
    print(neg_counter / length_of_list)
    print(zero_counter / length_of_list)


if __name__ == '__main__':
    # Input a list of numbers
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
