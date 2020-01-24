#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    # change input number to binary, then pad the string with leading zeros
    binary_n = format(n, 'b').zfill(32)
    transfer_bn = []
    for c in binary_n:
        if c == '1':
            transfer_bn.append('0')
        else:
            transfer_bn.append('1')

    return int(''.join(transfer_bn), 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
