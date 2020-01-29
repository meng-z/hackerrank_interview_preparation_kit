#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    curr = []
    curr.append(arr[0])
    curr.append(max(arr[:2]))

    for a in arr[2:]:
        curr.append(max([
            a, # only select a
            curr[-2] + a, # select a and max no-adjacent
            curr[-1] # do not select a
        ]))

    return curr[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
