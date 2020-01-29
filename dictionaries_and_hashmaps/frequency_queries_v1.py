#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
# Terminated due to timeout
def freqQuery(queries):
    ans = []
    curr = defaultdict(int)
    for query in queries:
        if query[0] == 1:
            curr[query[1]] += 1
        elif query[0] == 2:
            if curr[query[1]] > 0:
                curr[query[1]] -= 1
        else:
            if query[1] in curr.values():
                ans.append(1)
            else:
                ans.append(0)
    return ans
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
