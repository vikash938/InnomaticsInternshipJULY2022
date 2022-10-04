# List Comprehensions

#Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to . Here, . 
# Please use list comprehensions rather than multiple loops, as a learning exercise. Here,  0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

# Input Format
# Four integers x,y,z and n, each on a separate line.
# Constraints
# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]



x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
    
    
result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(result)