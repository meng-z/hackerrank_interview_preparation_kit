# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
#xs = list(map(int, input().split()[2:]))
#ys = list(map(int, input().split()[2:]))
xs = [15,12,8,8,7,7,7,6,5,3]
ys = [10,25,17,11,13,17,20,13,9,15]

n = len(xs)
xy_sum = sum([x*y for x, y in zip(xs, ys)])
x_sum = sum(xs)
y_sum = sum(ys)
x_square_sum = sum([x**2 for x in xs])
y_square_sum = sum([y**2 for y in ys])

corr = (n*xy_sum - x_sum*y_sum) / math.sqrt((n*x_square_sum - x_sum*x_sum)*(n*y_square_sum - y_sum*y_sum))
print(round(corr, 3))
