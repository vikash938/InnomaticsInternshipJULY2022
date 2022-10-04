# linear Algebra
import numpy as np

n = int(input())
arr = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(arr),2))