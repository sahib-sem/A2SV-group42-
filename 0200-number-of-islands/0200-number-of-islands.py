class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[1, 0] , [-1, 0] , [0, -1] , [0, 1]]
        
        def isValid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1'
        
        def dfs(row, col):
            
            grid[row][col] = '0'
            
            for x, y in directions:
                
                new_x, new_y = row + x , col + y
                
                if isValid(new_x, new_y):
                    dfs(new_x, new_y)
            
            
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        
        return count
        