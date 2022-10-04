# Zero and Ones 


import numpy as np

n = tuple(map(int, input().split()))

# for zero matrix
zero_matrix = np.zeros(n, int)
print(zero_matrix)
# for identity matrix
one_matrix = np.ones(n, int)
print(one_matrix)
