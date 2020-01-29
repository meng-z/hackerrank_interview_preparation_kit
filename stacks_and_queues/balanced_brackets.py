#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    matched = {')':'(', ']':'[', '}':'{'}
    stack = list()
    for e in s:
        if e in matched.values():
            stack.append(e)
        else:
            if len(stack) == 0 or stack.pop() != matched[e]:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
