#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    MAX_BRIBES = 2
    for i in range(len(q)-1, -1,-1):
        if q[i] - (i+1) > MAX_BRIBES:
            print('Too chaotic')
            return
        for j in range(max(0, q[i]-MAX_BRIBES), i):
            if q[j] > q[i]:
                count += 1

    print(count)

'''
# failed for test case
8
1 2 5 3 7 8 6 4
def minimumBribes(q):
    max_bribes = 2
    count = 0
    chaotic_flag = False 
    for i in range(len(q) - 1):
        diff = q[i] - q[i+1]
        if diff > 0:
            if diff <= max_bribes:
                count += diff
            else:
                chaotic_flag = True
                break

    if chaotic_flag:
        print('Too chaotic')
    else:
        print(count)
'''  

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

