#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
# 6/16 test cases failed
def abbreviation(a, b):
    # special case
    upper_in_a = [e for e in a if e.isupper()]
    for uia in upper_in_a:
        if uia not in b:
            return 'NO'

    ai, bi = 0, 0
    result = []
    a_upper = a.upper()
    while bi < len(b) and ai < len(a) and b[bi] in a_upper:
        if a[ai].upper() == b[bi]:
            result.append(a[ai].upper())
            ai += 1
            bi += 1 
        else:
            ai += 1
    print(result)
    if ''.join(result) == b and bi == len(b):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
