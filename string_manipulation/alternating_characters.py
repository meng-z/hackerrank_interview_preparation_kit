#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    if len(s) == 1:
        return 0

    count = 0
    curr = s[0]
    for i in range(len(s)-1):
        if s[i+1] == curr:
            count += 1
        else:
            curr = s[i+1]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

