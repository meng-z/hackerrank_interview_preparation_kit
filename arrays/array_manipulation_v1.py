#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
# Terminated due to timeout
def arrayManipulation(n, queries):
    ar = [0] * n
    for query in queries:
        a, b, k = query
        tmp = [0]*(a-1) + [k]*(b-a+1) + [0]*(n-b)
        ar = [i+j for i, j in zip(ar, tmp)]
    return max(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

