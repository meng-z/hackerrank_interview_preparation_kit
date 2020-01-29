#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    # start from the minimum days requited to product an item
    curr = min(machines)
    while True:
        # at the current day, how many items can be produced
        num = sum([(curr // machine) for machine in machines])
        if num < goal:
            curr += 1
        else:
            return curr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
