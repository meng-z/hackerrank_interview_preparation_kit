#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
# 4/20 test cases failed: e.g. 'aabbc'
def isValid(s):
    occur = Counter(s).most_common()
    min_occur = occur[-1][1]
    distinct_occur_num = len(set([oc[1] for oc in occur]))
    if distinct_occur_num > 2:
        return 'NO'
    if distinct_occur_num == 1:
        return 'YES'

    greater_than_min_occur = [oc for oc in occur if oc[1] > min_occur]
    if len(greater_than_min_occur) == 1 and greater_than_min_occur[0][1] - 1 == min_occur:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
