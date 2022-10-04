# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1: 

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.



# Solution

class Solution:
    def singleNumber(self, nums):

        result = 0
        for i in nums:
            result ^= i

        return result

object_1 = Solution()
nums = [4,1,2,1,2]
print(object_1.singleNumber(nums))




# Time complexity: O(n). We only iterate through nums so the time complexity is number of element in nums.
# Space complexity: O(1)



# Another Solution

class Solution:
    def singleNumber(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i]=1
        return hash_table.popitem()[0]



# Time complexity: O(n.1) = O(n). Time complexity of for loop O(n). Time complexity of hash table(dictionary in python) operation pop in O(1)
# Space complexity: O(n). The space required by hash_table is equal to the number of elements in nums. 