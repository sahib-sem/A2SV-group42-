class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        
        
        ans = 0
        
        for m in range(1, n + 1):
            
            
            diff = 2 * n - (m * (m - 1))
            
            if diff <= 0:
                break
                
            if diff % (2* m) == 0:
                ans += 1
                
        return ans
            
            