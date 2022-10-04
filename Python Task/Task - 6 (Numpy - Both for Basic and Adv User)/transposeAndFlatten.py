# Transpose and Flatten

import numpy

# n = rows and m = columns
n,m = map(int, input().split())

arr = numpy.array([input().strip().split() for i in range(n)], int)

print(arr.transpose())
print(arr.flatten())

