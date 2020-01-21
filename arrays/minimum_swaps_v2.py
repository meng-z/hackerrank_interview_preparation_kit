#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)

    idx = [i for i in range(n)]
    arr_pos = [(a, i) for a, i in zip(arr, idx)]
    arr_pos.sort(key=lambda x:x[0])

    visited = {i:False for i in range(n)}

    swaps = 0
    for i in range(n):
        if visited[i] or arr_pos[i][1] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1

        if cycle_size > 0:
            swaps += (cycle_size - 1)
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

