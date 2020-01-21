#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict = defaultdict(int)
    note_dict = defaultdict(int)
    for mag in magazine:
        mag_dict[mag] += 1

    for n in note:
        note_dict[n] += 1
        if n not in mag_dict.keys() or note_dict[n] > mag_dict[n]:
            print('No')
            return

    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

