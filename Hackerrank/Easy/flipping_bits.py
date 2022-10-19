#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    bin_a = bin(n)
    bin_a = bin_a[2:]
    bin_32 = (32 - len(bin_a)) * '0' + bin_a

    flipped_bin_32 = []

    for i in range(0, len(bin_32)):
        if bin_32[i] == "0":
            flipped_bin_32.append("1")
        else:
            flipped_bin_32.append("0")

    flipped_bin_32 = "".join(flipped_bin_32)

    dec_bin_32 = int(flipped_bin_32, 2)

    return dec_bin_32


if __name__ == '__main__':
    q = int(input().strip())

    result = flippingBits(q)
