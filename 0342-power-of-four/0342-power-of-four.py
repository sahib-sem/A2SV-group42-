class Solution:
    def isPowerOfFour(self, n: int) -> bool:
    
        def recursive(m):
            
            if m == 1.0:
                return True
            if m < 1: return False
          
            return recursive(m / 4)
        return recursive(n)
            
            
        
       
        
        