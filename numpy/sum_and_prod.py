import numpy

n, m = list(map(int, input().strip().split()))

a = []
for _ in range(n):
    a.append(list(map(int, input().strip().split())))

na = numpy.array(a)
na_sum_a0 = numpy.sum(na, axis=0)
print(numpy.prod(na_sum_a0))
