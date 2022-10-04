# identity
import numpy

n, m = map(int, input().split())

# identity matrix
output = str(numpy.eye(n,m))
print(output.replace("0"," 0").replace("1"," 1"))