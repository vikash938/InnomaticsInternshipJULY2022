# array mathematics

import numpy

# n for rows and m for columns
n, m = map(int, input("Enter n or m value: ").split()) 

# a, b are numpy array
a, b = (numpy.array([input("Enter something : ").split() for _ in range(n)], int) for i in range(2))


print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')