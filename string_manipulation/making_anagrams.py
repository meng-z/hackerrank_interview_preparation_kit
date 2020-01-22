#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_chars = sorted([char for char in a])
    b_chars = sorted([char for char in b])

    a_idx, b_idx = 0, 0
    common = []
    while a_idx < len(a_chars) and b_idx < len(b_chars):
        if a_chars[a_idx] > b_chars[b_idx]:
            b_idx += 1
        elif a_chars[a_idx] < b_chars[b_idx]:
            a_idx += 1
        else:
            common.append(a_chars[a_idx])
            a_idx += 1
            b_idx += 1
    
    ans = (len(a_chars) - len(common)) + (len(b_chars) - len(common))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

