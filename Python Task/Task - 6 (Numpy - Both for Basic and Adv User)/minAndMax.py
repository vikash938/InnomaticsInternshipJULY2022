# min and max

import numpy as np

n, m = list(map(int, input("Enter n or m value: ").split()))

arr = np.array([input("Enter Something: ").split() for _ in range(n)], int)
minAxis = np.min(arr, axis=1)
print(max(minAxis))