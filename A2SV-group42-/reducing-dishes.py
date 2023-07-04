class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        
        #dp 
        satisfaction.sort()
        
        # [-9, -8 , -1, 0, 5]
        memo = {}
        
        def dp(i , time):
            
            if i == len(satisfaction):
                return 0
            
            state = (i , time)
            
            if state not in memo:
                
                memo[state] = max(satisfaction[i] * time + dp(i + 1, time + 1) , dp(i + 1, time))
            
            return memo[state]
        
        return dp(0, 1)
                
            
            