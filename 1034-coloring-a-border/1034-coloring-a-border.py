class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        directions = [[1, 0], [-1, 0] , [0, -1] , [0, 1]]
        
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        visited = set()
        new_grid = []
        for r in range(len(grid)):
            temp = []
            for c in range(len(grid[0])):
                temp.append(grid[r][c])
            new_grid.append(temp)
        
        def dfs(row, col, clr):
            if not isValid(row, col):
                return 0
            
            if grid[row][col] != clr:
                return 0
            
            if (row, col) in visited:
                return 1
            
            visited.add((row, col))
            
            for change_x, change_y in directions:
                
                new_x, new_y = row + change_x  , col + change_y
                
                res = dfs(new_x, new_y, clr)
                if res == 0:
                    new_grid[row][col] = color
        
        dfs(row, col, grid[row][col])
        
        return new_grid
            
            