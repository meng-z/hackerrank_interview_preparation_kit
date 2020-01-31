# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import numpy as np
from collections import defaultdict

N = int(input())
arr = np.array(list(map(int, input().split())))

mean = arr.mean()
print(round(mean, 1))

# note that 'numpy.ndarray' object has no attribute 'median', so we cannot use arr.median()
median = np.median(arr)
print(round(median, 1))

# find mode
dic = defaultdict(int)
for a in arr:
    dic[a] += 1
# sort by value(DSC) then by key(ASC), return a list of tuples
sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dic[0][0])

std = arr.std()
print(round(std, 1))

# calculate the confidence interval
lower = mean - 1.96 * (std / math.sqrt(N))
upper = mean + 1.96 * (std / math.sqrt(N))
print('{} {}'.format(round(lower, 1), round(upper, 1)))
