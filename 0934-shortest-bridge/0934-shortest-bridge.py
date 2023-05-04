class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # 0 1 0  
        # 0 0  0
        # 0 0  1
        # find one of the island the perform a bfs 
        directions = [[1,0], [-1, 0], [0, -1], [0, 1]]
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid)
        island1 = []
        def dfs(x, y, visited):
            nonlocal island1
            island1.append((x, y))
            visited.add((x, y))
            
            for ch_x, ch_y in directions:
                n_x, n_y = ch_x + x , ch_y + y
                
                if inbound(n_x, n_y ) and grid[n_x][n_y] and (n_x, n_y) not in visited:
                    dfs(n_x, n_y , visited)
        n = len(grid)
        found  = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c, set())
                    found = True
                    break
            if found:
                break
                    
        queue = deque(island1)
        visited = set(island1)
        level = 0
        done = False
        
        while queue:
            
            length = len(queue)
        
            for _ in range(length):
                x, y= queue.popleft()
               
                for ch_x, ch_y in directions:
                    new_x, new_y = x + ch_x , y + ch_y
                    if inbound(new_x , new_y) and (new_x, new_y) not in visited:
                        if grid[new_x][new_y] == 1:
                            return level
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
                
            level += 1
            
        
         
        
                    
        
                
            
        
        
        
        