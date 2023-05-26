class Solution:
    
    def climbStairs(self, n: int) -> int:
        self.arr = {}
        
        def Dp(n):
            if n <= 2:
                return n
            if n not in self.arr:
                self.arr[n] = Dp(n- 1) + Dp(n- 2)
            
            return self.arr[n]
        
        return Dp(n)
        
        