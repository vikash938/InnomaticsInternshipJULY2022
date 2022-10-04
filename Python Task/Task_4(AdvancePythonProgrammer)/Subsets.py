#  Problem : Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# Solutions

from itertools import combinations
def subsets(nums):
        
    listOfSubsets = []
        
    for i in range(len(nums)+1):
        listOfSubsets  += [list(j) for j in combinations(nums, i)]
    return listOfSubsets

nums = [1,2,3]
print(subsets(nums))