# floor


import numpy as np

#These options determine the way floating point numbers, arrays and other NumPy objects are displayed.
np.set_printoptions(sign = ' ')

arr = np.array(input().split(), float)


print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
