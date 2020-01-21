#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
# Terminated due to timeout
def twoStrings(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    flag = False
    if l1 < l2:
        for i in range(l1):
            for j in range(1, l1-i):
                if s1[i:i+j] in s2:
                    flag = True
                    break
    else:
        for i in range(l2):
            for j in range(1, l2-i):
                if s2[i:i+j] in s1:
                    flag = True
                    break
    if flag:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

