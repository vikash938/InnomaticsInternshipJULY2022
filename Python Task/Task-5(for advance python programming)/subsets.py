# subsets

from itertools import combinations
class Solution:
    def subsets(self, nums):
        
        listOfSubsets = []
        
        for i in range(len(nums)+1):
            listOfSubsets  += [list(j) for j in combinations(nums, i)]
        return listOfSubsets
        
object_1 = Solution()
nums = [1,2,3]

print(object_1.subsets(nums))

