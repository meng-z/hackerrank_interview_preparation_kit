import numpy

n, m = list(map(int, input().strip().split()))
a = []

for _ in range(n):
    a.append(list(map(int, input().strip().split())))

na = numpy.array(a)
na_min_a1 = numpy.min(na, axis=1)
print(numpy.max(na_min_a1))
