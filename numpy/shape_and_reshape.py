import numpy

arr = list(map(int, input().strip().split()))

np_arr = numpy.array(arr)
ans = numpy.reshape(np_arr, (3, 3))
print(ans)
