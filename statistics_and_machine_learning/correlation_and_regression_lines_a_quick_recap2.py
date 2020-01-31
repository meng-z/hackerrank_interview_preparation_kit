# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def corr(xs, ys):
    n = len(xs)
    xy_sum = sum([x*y for x, y in zip(xs, ys)])
    x_sum = sum(xs)
    y_sum = sum(ys)
    x_square_sum = sum([x**2 for x in xs])
    y_square_sum = sum([y**2 for y in ys])

    corr = (n*xy_sum - x_sum*y_sum) / math.sqrt((n*x_square_sum - x_sum*x_sum)*(n*y_square_sum - y_sum*y_sum))
    return corr

def std(xs):
    n = len(xs)
    x_sum = sum(xs)
    x_mean = x_sum / n
    tmp = sum([(x-x_mean)**2 for x in xs])
    std = math.sqrt(tmp/n)
    return std

xs = [15,12,8,8,7,7,7,6,5,3]
ys = [10,25,17,11,13,17,20,13,9,15]

r = corr(xs, ys)
x_std = std(xs)
y_std = std(ys)

slope = r * (y_std/x_std)
print(round(slope, 3))
