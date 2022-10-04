#single Number II


from typing import Counter


class Solution:
    def singleNumber(self, nums):
        # nums ---> list of integers type
        
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k

obj = Solution()
nums = [1,3,2,3,3,1,3,2]
print(obj.singleNumber(nums))
        