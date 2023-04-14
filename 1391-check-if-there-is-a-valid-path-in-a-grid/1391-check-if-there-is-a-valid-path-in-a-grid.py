class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1) , (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0) , (0, 1)]
            
        }
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        destination = (len(grid) - 1 , len(grid[0]) - 1)
        
        def dfs(row, col, visited):
            
            if (row, col) == destination:
                return True
            
            visited.add((row, col))
            
            for x , y in directions[grid[row][col]]:
                new_row = row + x
                new_col = col + y
                
                if inbound(new_row, new_col) and not (new_row, new_col) in visited and (-x, -y) in directions[grid[new_row][new_col]]:
                    if dfs(new_row, new_col , visited):
                        return True
            
            return False
            
        
        return dfs(0 , 0 , set())
                    
            
            
        
        
        