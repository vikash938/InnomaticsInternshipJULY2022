# mean var and std

import numpy as np

# n for rows and m for columns
n, m  = list(map(int, input("Enter n and m value: ").split()))

arr = np.array([input().split() for _ in range(n)], int)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr, axis=None), 11))


