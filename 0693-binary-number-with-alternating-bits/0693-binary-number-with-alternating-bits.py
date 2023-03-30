class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        check = n & 1
        
        while n:
            if 1 & (n) != check:
                return False
            check = 0 if check == 1 else 1
            n >>= 1
            
        return True
            
        