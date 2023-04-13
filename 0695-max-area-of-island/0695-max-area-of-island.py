class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[1, 0] , [-1, 0] , [0, 1], [0, -1]]
        
        
        def isValid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def explore(pos, visited):
            
            stack = [pos]
            count = 0
            visited.add(pos)
            while stack:
                
                curr_x , curr_y = stack.pop()
                
                
                count += 1
                
                for direction in directions:
                    change_x, change_y = direction
                    n_x, n_y = curr_x + change_x , curr_y + change_y
                    if isValid(n_x, n_y) and grid[n_x][n_y] == 1 and (n_x, n_y) not in visited:
                        stack.append((n_x, n_y)) 
                        visited.add((n_x, n_y))      
                        
            return [visited, count]
        
        max_area = 0   
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    
                    visited , count = explore((r, c), visited)
                    max_area = max(max_area, count)
        
        return max_area