#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    path = [0]
    length = len(c)
    curr = 0
    while True:
        if curr + 2 < length and c[curr + 2] == 0:
            curr += 2            
        else:
            curr += 1

        if curr < length:
            path.append(curr)
        else:
            break

    return len(path) - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

