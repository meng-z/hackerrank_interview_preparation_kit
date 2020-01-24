import numpy

shape = list(map(int, input().strip().split()))
print(numpy.zeros(tuple(shape), dtype=int))
print(numpy.ones(tuple(shape), dtype=int))
