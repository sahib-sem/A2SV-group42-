class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = {}
        
        def dp(i, main_idx):
            
            if main_idx == len(triangle) - 1:
                
                return triangle[main_idx][i] 
                
            
            state = (i, main_idx)
            
            if state not in memo:
                
                memo[state] = triangle[main_idx][i] + min(dp(i , main_idx + 1) , dp(i + 1, main_idx + 1))
            
            return memo[state]
        
        
        
        return dp(0, 0)
        