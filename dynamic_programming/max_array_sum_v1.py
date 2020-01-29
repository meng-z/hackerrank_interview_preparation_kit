#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
# Terminated due to timeout
def maxSubsetSum(arr):
    curr = float('-inf')

    for skip in range(2, len(arr)):
        for i, a in enumerate(arr):
            tmp = arr[i::skip]
            if len(tmp) > 1 and sum(tmp) > curr:
                curr = sum(tmp)
    return curr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
