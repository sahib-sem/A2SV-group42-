class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        f1=1
        f2=2
        f3=0
        x=2
        while x< n:
            f3=f1+f2
            f1=f2
            f2=f3
            
            x+=1
        return f3
        