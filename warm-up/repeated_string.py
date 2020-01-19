#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    occur_in_s = s.count('a')
    num_of_entire_s = n // len(s)
    partial_of_s = n % len(s)
    return occur_in_s * num_of_entire_s + s[:partial_of_s].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

