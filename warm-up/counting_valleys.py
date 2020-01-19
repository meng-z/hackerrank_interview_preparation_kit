#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    prev_sum = 0
    current_sum = 0
    valley_count = 0
    for c in s:
        prev_sum = current_sum
        if c == 'U':
            current_sum += 1
        else:
            current_sum -= 1
        if current_sum == 0 and prev_sum < 0:
            valley_count += 1
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

