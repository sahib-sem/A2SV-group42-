class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # res = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        directions = [[1, 0], [0, 1] , [-1, 0] , [0, -1]]
        
        
        def inbound(x, y):
            return 0 <= x < len(mat) and 0 <= y < len(mat[0])
        queue = deque()
        visited = set()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        steps = 0
        while queue:
            
            length = len(queue)
            steps += 1
            
            for _ in range(length):
                x, y = queue.popleft()
                for change_x, change_y in directions:
                    new_x, new_y = x + change_x , y + change_y
                    if inbound(new_x, new_y) and (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        
                        mat[new_x][new_y] = steps
                        visited.add((new_x, new_y))
        
        return mat
                        
                    
                    
    
            
            
        