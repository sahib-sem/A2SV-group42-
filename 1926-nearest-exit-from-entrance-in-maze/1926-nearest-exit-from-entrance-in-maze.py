class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        queue = deque([entrance])
        visited = set({(entrance[0], entrance[1])})
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def isValid(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != '+'
        
        level = 0
        
        while queue:
            
            length = len(queue)
            
            for _ in range(length):
                
                x, y = queue.popleft()
                if maze[x][y] == '.' and (x in [0, len(maze) - 1] or y in [0, len(maze[0]) - 1]) and entrance != [x, y]:
                    return level
                for ch_x, ch_y in directions:
                    nx , ny = ch_x + x , ch_y + y
                    
                    if isValid(nx, ny) and (nx, ny) not in visited:
                        
                        queue.append([nx, ny])
                        visited.add((nx, ny))
            level += 1
            
        
        return - 1
                
                
            
            
                
        