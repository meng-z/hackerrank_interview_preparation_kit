#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
# 5/7 test cases failed
def sherlockAndAnagrams(s):
    print('query', s)
    count = 0
    visited = set()
    for i in range(len(s)):
        for j in range(1, len(s)-i):
            curr = s[i:i+j]
            reversed_curr = curr[::-1]
            print(curr, reversed_curr)
            if len(set(curr)) == 1:
                target = s[:i] + s[i+j:]
            else:
                target = s
            print('target', target)
            if curr not in visited and reversed_curr in target:
                print('ans', curr)
                count += 1
            visited.add(curr)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

