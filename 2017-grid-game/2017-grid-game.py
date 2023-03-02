class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        topSum = sum(grid[0])
        ans = math.inf
        bottomSum = 0
        n = len(grid[0])
        
        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans , max(topSum , bottomSum))
            bottomSum += grid[1][i]
            
        return ans
        
                    
                    
                    
                    
            
            
            
        
        
                