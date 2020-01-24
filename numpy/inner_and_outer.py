import numpy

a = numpy.array(list(map(int, input().strip().split())))
b = numpy.array(list(map(int, input().strip().split())))

print(numpy.inner(a, b))
print(numpy.outer(a, b))
