#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

# Complete the pairs function below.
# Terminated due to timeout
def pairs(k, arr):
    diff = [a - k for a in arr]
    counter = Counter(arr)
    diff_occur_in_arr = {k:v for k, v in counter.items() if k in diff}
    ans = sum(diff_occur_in_arr.values())

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
