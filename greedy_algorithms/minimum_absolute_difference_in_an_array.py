#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    ans = float('inf')

    for i in range(len(sorted_arr) - 1):
        curr_diff = sorted_arr[i+1] - sorted_arr[i]
        if curr_diff < ans:
            ans = curr_diff
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
