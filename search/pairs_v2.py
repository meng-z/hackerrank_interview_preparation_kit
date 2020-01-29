#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the pairs function below.
def pairs(k, arr):
    sorted_arr = sorted(arr)
    visited = defaultdict(int)
    count = 0
    for a in sorted_arr:
        target = a - k
        if target in visited.keys():
            count += visited[target]
            visited[a] += 1
        else:
            visited[a] += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
