# dot and cross product

import numpy as np

# n for rows and m for columns
n = int(input())
arr_1 = np.array([input().split() for i in range(n)], dtype=int)
arr_2 = np.array([input().split() for i in range(n)], dtype=int)
 

print(np.dot(arr_1, arr_2))
