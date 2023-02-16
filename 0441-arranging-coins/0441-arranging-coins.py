class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair=1
        complete_stair=0
        while n>0:
            if n>=stair:
                complete_stair+=1
            n-=stair
            stair+=1
        return complete_stair
            
            
            
        