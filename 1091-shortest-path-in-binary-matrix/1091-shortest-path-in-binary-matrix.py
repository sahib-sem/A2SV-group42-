class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [[0, 1], [1, 0] , [-1, 0], [0, -1] , [1, -1] , [-1, 1], [-1, -1] , [1, 1]]
        
        def isValid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0
        
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1]:
            return -1
        
        
        queue = deque([(0, 0)])
        grid[0][0] = 1
        steps = 0
        reach_final = False
        
        while queue:
            
            steps += 1
            for _ in range(len(queue)):
                curr_x , curr_y  = queue.popleft()
                if curr_x == len(grid) -1  and curr_y == len(grid[0]) - 1:
                    return steps
                for x, y in directions:
                    new_x, new_y = x + curr_x , y + curr_y

                    if isValid(new_x , new_y):
                        grid[new_x][new_y] = 1
                        queue.append((new_x , new_y))
                        
        return -1
                    
            