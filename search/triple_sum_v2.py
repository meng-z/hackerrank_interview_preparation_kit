#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    # make sure that a, b and c are sorted
    # note that we want to get the number of distinct triplets, so take set of each list first
    sorted_a = sorted(set(a))
    sorted_b = sorted(set(b))
    sorted_c = sorted(set(c))

    ai, bi, ci = 0, 0, 0
    ans = 0
    # for each element in sorted_b, how many items in sorted_a and sorted_b are smaller than it, respectively
    while bi < len(sorted_b):
        # since they are sorted, no necessary to reset ai, ci to 0
        while ai < len(sorted_a) and sorted_a[ai] <= sorted_b[bi]:
            ai += 1
        while ci < len(sorted_c) and sorted_c[ci] <= sorted_b[bi]:
            ci += 1
        ans += ai * ci
        bi += 1

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
