import numpy

n = int(input())
a, b = [], []

for _ in range(n):
    a.append(list(map(int, input().strip().split())))

for _ in range(n):
    b.append(list(map(int, input().strip().split())))

na = numpy.array(a)
nb = numpy.array(b)

print(numpy.dot(na, nb))
