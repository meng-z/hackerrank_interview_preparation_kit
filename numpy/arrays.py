import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    ans = numpy.array(arr[::-1], dtype=float)
    return ans

arr = input().strip().split(' ')
