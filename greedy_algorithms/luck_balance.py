#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    # sort by luck in descending order
    sorted_contests = sorted(contests, key=lambda x:x[0], reverse=True)
    count = 0
    balance = 0
    for sc in sorted_contests:
        # if the contest is unimportant, just lose
        if sc[1] == 0:
            balance += sc[0]
        else:
            # still able to lose important contest
            if count < k:
                balance += sc[0]
                count += 1
            else:
                balance -= sc[0]
    return balance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
