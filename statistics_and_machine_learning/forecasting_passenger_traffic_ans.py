# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
import scipy.interpolate
import random

n = int(input())
num=[]
for i in range(int(n)):
    l = input()
    l_l = l.split()
    num.append(int(l_l[1]))

# create some normally distributed values and make a histogram
a = numpy.array(num)
counts, bins = numpy.histogram(a, bins=10, density=True)
cum_counts = numpy.cumsum(counts)
bin_widths = (bins[1:] - bins[:-1])

# generate more values with same distribution
x = cum_counts*bin_widths
y = bins[1:]
inverse_density_function = scipy.interpolate.interp1d(x, y)
b = numpy.zeros(n+12)

for i in range(len(b)):
    u = random.uniform(x[0], x[-1])
    b[i] = inverse_density_function(u)


solution=[]
for i in range(12):
    u = random.uniform(x[0], x[-1])
    solution.append(inverse_density_function(u))

for i in solution:
    print (i)
