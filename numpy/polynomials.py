import numpy

coeff = numpy.array(list(map(float, input().strip().split())))
idx = int(input())
print(numpy.polyval(coeff, idx))
