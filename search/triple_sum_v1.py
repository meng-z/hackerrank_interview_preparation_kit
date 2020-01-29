#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
# Terminated due to timeout
def triplets(a, b, c):
    # make sure that a, b and c are sorted
    # note that we want to get the number of distinct triplets, so take set of each list first
    sorted_a = sorted(set(a))
    sorted_b = sorted(set(b))
    sorted_c = sorted(set(c))

    possible = list()
    # for each element in sorted_b, how many items in sorted_a and sorted_b are smaller than it, respectively
    for sb in sorted_b:
        count_a = 0
        count_c = 0
        for sa in sorted_a:
            if sa <= sb:
                count_a += 1
            else:
                break
        for sc in sorted_c:
            if sc <= sb:
                count_c += 1
            else:
                break
        possible.append((count_a, count_c))

    ans = 0
    for p in possible:
        ans += (p[0] * p[1])
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
