# Concatenate


import numpy

n,m,p=map(int,input().split())

arr_1 = numpy.array([input().strip().split() for i in range(n)], int)
arr_2 = numpy.array([input().strip().split() for i in range(m)], int)


print(numpy.concatenate((arr_1, arr_2), axis = 0))