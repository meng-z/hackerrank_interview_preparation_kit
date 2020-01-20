#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

# Complete the arrayManipulation function below.
# Runtime Error
def arrayManipulation(n, queries):
    result = defaultdict(int)
    for query in queries:
        a, b, k = query
        for i in range(a, b+1):
            result[i] += k
    return max(result.values())

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

