#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)+1):
        dic = defaultdict(int)
        for j in range(len(s)-i+1):
            curr = ''.join(sorted(s[j:j+i]))
            dic[curr] += 1

        for k, v in dic.items():
            count += (v*(v-1)) // 2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

