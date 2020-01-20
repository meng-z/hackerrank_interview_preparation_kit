#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# Terminated due to timeout
def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            j = arr.index(i+1)
            arr[i], arr[j] = i+1, arr[i]
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

