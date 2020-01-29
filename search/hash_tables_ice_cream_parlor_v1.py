#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
# Runtime Error
def whatFlavors(cost, money):
    # create a list of tuple to keep original index of each flavor, together with its cost
    idx_cost = [(idx, c) for idx, c, in zip(range(1, len(cost)+1), cost)]
    # sort by cost
    sorted_idx_cost = sorted(idx_cost, key=lambda x:x[1])

    candidates = dict()
    # search from the cheapest flavor
    for i in range(len(sorted_idx_cost) - 1):
        for j in range(i + 1, len(sorted_idx_cost)):
            if sorted_idx_cost[j][1] >= money:
                break
            curr_sum = sorted_idx_cost[i][1] + sorted_idx_cost[j][1]
            if curr_sum <= money:
                # since there is always a unique solution, ignore duplicate key problem
                if sorted_idx_cost[i][0] < sorted_idx_cost[j][0]:
                    candidates[curr_sum] = (sorted_idx_cost[i][0], sorted_idx_cost[j][0])
                else:
                    candidates[curr_sum] = (sorted_idx_cost[j][0], sorted_idx_cost[i][0])
    
    max_spent = max(candidates.keys())
    print(candidates[max_spent][0], candidates[max_spent][1])

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
