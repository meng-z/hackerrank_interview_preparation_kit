import numpy

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(float, input().strip().split())))

na = numpy.array(a)
print(numpy.round(numpy.linalg.det(na), 2))
