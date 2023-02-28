class Solution:
    def isPowerOfFour(self, n: int) -> bool:
    
        def recursive(m):
            if m == 0:
                return False
            if m == 1:
                return True
            if m % 4 == 0:
                return recursive(m // 4)
        return recursive(n)
            
            
        
       
        
        