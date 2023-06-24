class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = {}
         
        def dp(r, c):
            
            if not ((0 <= r < len(grid)) and (0 <= c < len(grid[0]))):
                return float('inf')
            
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]
            
            state = (r, c)
            
            if state not in memo:
                
                memo[state] = grid[r][c] + min (dp(r + 1, c) , dp(r, c + 1))
            
            return memo[state]
        
        return dp(0, 0)
            
        