class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        
        #dp 
#         satisfaction.sort()
        
#         # [-9, -8 , -1, 0, 5]
#         memo = {}
        
#         def dp(i , time):
            
#             if i == len(satisfaction):
#                 return 0
            
#             state = (i , time)
            
#             if state not in memo:
                
#                 memo[state] = max(satisfaction[i] * time + dp(i + 1, time + 1) , dp(i + 1, time))
            
#             return memo[state]
        
#         return dp(0, 1)

        # greedy 
        satisfaction.sort()
        n = len(satisfaction)
        total = 0
        max_val = 0
        
        for i in range(1, n + 1):
            total += satisfaction[i - 1] * i
            
        max_val = max(total, max_val)
        
        sub = sum(satisfaction)
        
        for j in range(1, n):
            
            total -= sub
            max_val = max(total, max_val)
            sub -= satisfaction[j - 1]
        
        return max_val
            
            
            
        
                
            
            