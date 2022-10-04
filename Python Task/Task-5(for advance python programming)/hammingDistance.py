
# hamming distance


class Solution:
    def hammingDistance(self, x, y):
        # type x --> int
        # type y --> int
        result = 0
        for _ in range(32):
            first_bit = x % 2 
            second_bit = y % 2
            if first_bit != second_bit:
                result += 1
            x = x >> 1
            y = y >> 1
        return result
obj = Solution()
x = 1
y = 4
print(obj.hammingDistance(x,y))