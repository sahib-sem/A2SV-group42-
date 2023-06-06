class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}
        
        def trib(n):
            if n <= 1:
                return n
            if n == 2:
                return 1
            
            if n not in memo:
                memo[n] = trib(n-1) + trib(n-2) + trib(n-3)
            
            return memo[n]
        
        return trib(n)

        
        