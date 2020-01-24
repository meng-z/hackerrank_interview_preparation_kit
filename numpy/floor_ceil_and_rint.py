import numpy

a = numpy.array(list(map(float, input().strip().split())))

# because of the test case bug
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
