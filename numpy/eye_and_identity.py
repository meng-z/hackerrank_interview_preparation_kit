import numpy

n, m = list(map(int, input().strip().split()))

# because of the test case bug
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(n, m, k=0))
