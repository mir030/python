#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if "AM" in s:
        if s[0:2] == "12":
            new_time = "00"
            for letter in s[2:]:
                new_time += letter
            output = new_time[0:8]
            return output
        output = s[0:8]

    elif "PM" in s:
        if s[0:2] == "12":
            output = s[0:8]
            return output
        new_time = str(int(s[0:2]) + 12)
        for letter in s[2:]:
            new_time += letter
        output = new_time[0:8]

    return output


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

