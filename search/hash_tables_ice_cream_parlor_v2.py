#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    visited = {}
    for i, c in enumerate(cost):
        target = money - c
        if target in visited.keys():
            print(visited[target], i + 1)
        else:
            visited[c] = i + 1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
