# # lists 

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example



# N = 4
# append 1
# append 2
# append 3 1
# print

# append 1 : Append 1 to the list, arr = [1].
# append 2 : Append 2 to the list, arr = [1,2].
# insert 3 1: Insert 3 at index 1, arr = [1,3,2].
# print: Print the array.
# Output:
# [1, 3, 2]
# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]




# Enter your code here. Read input from STDIN. Print output to STDOUT
list = []
n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 3:
        eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("list." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print(list)
    else:
        eval("list." + a[0] + "()")