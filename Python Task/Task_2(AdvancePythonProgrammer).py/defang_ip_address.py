# Problem : Defanging IP address





# Solution 
class Solution(object):
    def defangIPaddr(self, address):
        
        """
        type address : str,
        rtype str
        """
    
        
        
        result = []
        for c in address:
            if c == '.':
                result.append("[.]")
            else:
                result.append(c)
        return "".join(result)
    
object_1 = Solution()
print(object_1.defangIPaddr("255.100.50.0"))