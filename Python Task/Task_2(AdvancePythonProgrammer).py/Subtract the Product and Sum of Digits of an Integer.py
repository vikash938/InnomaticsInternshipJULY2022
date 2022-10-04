# Subtract the Product and Sum of Digits of an Integer


# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 

# Constraints:

# 1 <= n <= 10^5





# Solution
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        num = str(n)
        product_of_digit = 1
        sum_of_digit = 0
        
        for number in num:
            int_n = int(number)
            product_of_digit *= int_n % 10
            sum_of_digit += int_n
            
            result = product_of_digit - sum_of_digit
        
        return result
    
object_1 = Solution()
n = 234
print(object_1.subtractProductAndSum(n))