import numpy

n, m = list(map(int, input().strip().split()))
a = []

for _ in range(n):
    a.append(list(map(int, input().strip().split())))

na = numpy.array(a)

# because of the test case bug
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(na, axis=1))
print(numpy.var(na, axis=0))
print(numpy.std(na, axis=None))
