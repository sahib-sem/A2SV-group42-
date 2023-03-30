class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        temp = x ^ y 
        
        count = 0
        while temp:
            if temp & 1:
                count += 1
            
            temp >>= 1
        
        return count 
        