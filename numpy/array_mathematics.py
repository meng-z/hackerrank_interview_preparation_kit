import numpy

n, m = list(map(int, input().strip().split()))

a, b = [], []
for _ in range(n):
    a.append(list(map(int, input().strip().split())))

for _ in range(n):
    b.append(list(map(int, input().strip().split())))

na = numpy.array(a)
nb = numpy.array(b)
print(na+nb)
print(na-nb)
print(na*nb)
print(na//nb)
print(na%nb)
print(na**nb)
