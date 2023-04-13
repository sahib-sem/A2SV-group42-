class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [[1, 0] , [-1, 0] , [0, 1], [0, -1]]
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        
        self.ans = 0  
        
        def isValid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def dfs(pos):
            c_x, c_y = pos
            if not isValid(c_x , c_y):
                return 1
            
            if grid[c_x][c_y] == 0:
                return 1
            if visited[c_x][c_y]:
                return 0
            
            
            
            
            visited[c_x][c_y] = 1
            
            for direction in directions:
                x, y = direction
                n_x, n_y = c_x + x , c_y + y
                res = dfs((n_x, n_y))
                self.ans += res
            
            return 0
                
        
        pos = 0          
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    pos = (r, c)
                    break
            if pos:
                break
        
        dfs(pos)
                
        return self.ans 
            
            

        
        
                
                
                
        
        