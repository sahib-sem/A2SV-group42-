class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0] , [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        
        def check():
            count = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        return False
        
         
            return True
        
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        steps = 0 if len(queue) > 0 else 1
        while queue:
            count_len = len(queue)
            steps += 1
            for _ in range(count_len):
                curr_x, curr_y = queue.popleft()
                
                for x, y in directions:
                    new_x , new_y = curr_x + x , curr_y + y
                    
                    if inbound(new_x , new_y) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
                        
        return steps - 1 if check() else -1
                    
                    