import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])
queries = []

for _ in range(n):
    queries.append(list(map(int, input().strip().split())))

a = numpy.array(queries)
print(numpy.transpose(a))
print(a.flatten())
