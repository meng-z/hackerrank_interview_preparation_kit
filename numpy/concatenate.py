import numpy

n, m, p = list(map(int, input().strip().split()))

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().strip().split())))

for _ in range(m):
    b.append(list(map(int, input().strip().split())))

print(numpy.concatenate((a, b), axis=0))
