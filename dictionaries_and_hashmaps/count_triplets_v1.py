#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
# Failed to pass some test cases.
def countTriplets(arr, r):
    occur = Counter(arr)
    sorted_arr = sorted(arr)
    count = 0

    # special case
    if len(arr) < 3:
        return 0
    if len(occur) == 1:
        if r != 1:
            return 0
        count = (len(arr) * (len(arr) - 1) * (len(arr) -2)) / (3 * 2)
        return int(count)

    for a, freq in occur.items():
        if a*r*r > sorted_arr[-1]:
            break
        if a*r in occur.keys() and a*r*r in occur.keys():
            count += freq * occur[a*r] * occur[a*r*r]
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
