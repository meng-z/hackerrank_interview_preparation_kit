#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    occur = Counter(s).most_common()
    distinct_occur = Counter([oc[1] for oc in occur]).most_common()

    if len(distinct_occur) == 1:
        return 'YES'
    if len(distinct_occur) > 2:
        return 'NO'

    if (1, 1) in distinct_occur:
        return 'YES'
    else:
        if abs(distinct_occur[0][0] - distinct_occur[1][0]) == 1 and (min(distinct_occur[0][1], distinct_occur[1][1]) == 1):
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
