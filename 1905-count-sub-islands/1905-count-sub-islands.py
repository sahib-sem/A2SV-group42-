class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # approach
        # find any island in grid2 the points used to represent this island check if they are part of an island in grid1
        directions = [[1,0], [-1,0] , [0,1], [0,-1]]
        def isValid(r, c):
            return 0 <= r < len(grid2) and 0 <= c < len(grid2[0]) and grid2[r][c] == 1
        
        def dfs(row, col, possible):
            grid2[row][col] = 0
            
            for x, y in directions:
                n_x , n_y = row + x , col + y
                
                if isValid(n_x, n_y):
                    if not dfs(n_x , n_y, possible) or not possible:
                        possible = False
                    if not grid1[n_x][n_y] == 1:
                        possible = False
                    
            return possible
        
        count = 0
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid1[row][col] and grid2[row][col]:
                    if dfs(row, col, True):
                        count += 1
        
        return count
                
            
            
            
        