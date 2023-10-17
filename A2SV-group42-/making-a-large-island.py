class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 1
        
        def componentSize(x, y, visited):
            
            if (x, y) in visited:
                return 0 
            
            ans = 1
            
            visited.add((x, y))
            
            for ch_x, ch_y in [(0, 1) , (1, 0) , (0, -1), (-1, 0)]:
                if valid(ch_x + x, ch_y + y):
                    ans += componentSize(x + ch_x, y + ch_y, visited)
            
            return ans
                
        def change_size(visited, size, id_):
                          
            for x, y in visited:
                grid[x][y] = (size, id_)
        
        global_visited = set({})
        id_ = 1
        for r in range(len(grid)):
            for c in range(len(grid)):
                
                if (r, c) not in global_visited and grid[r][c] == 1:
                          
                    visited = set({})

                    size = componentSize(r, c, visited)
                    
                    global_visited |= visited
                    
                    change_size(visited, size, id_)
                    id_ += 1
                elif grid[r][c] == 0:
                    grid[r][c] = (0, 0)
        
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                
                if grid[r][c][0] == 0:
                    curr = 1
                    used = set({})
                    for ch_x, ch_y in [(0, 1) , (1, 0) , (0, -1), (-1, 0)]:
                        
                        new_x, new_y = ch_x + r, ch_y + c
                        
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid):
                            
                            
                            val, id_ = grid[new_x][new_y]
                            if id_ not in used:
                                used.add(id_)
                                curr += val
                
                    ans = max(ans, curr)
                
                val, id_ = grid[r][c]
                
                ans = max(ans, val)
        
        
        return ans                    
                            
                    
                          
                          
                          
            
        
                          
        
        
        