class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        queue = deque([(tuple(board[0]), tuple(board[1]))])
        visited = set({(tuple(board[0]), tuple(board[1]))})
        def is_solved(board):
            if board[0] == (1, 2, 3) and board[1] == (4, 5, 0):
                return True
            
        def inbound(x, y):
            return 0 <= x < 2 and 0 <= y < 3
        def find_zero(board):
            for r in range(2):
                for c in range(3):
                    if board[r][c] == 0:
                        return (r, c)
        
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        level = 0
        
        while queue:
            
            length = len(queue)
           
            for _ in range(length):
                current = queue.popleft()
                if is_solved(current):
                    return level
                x, y = find_zero(current)
                
                for ch_x, ch_y in directions:
                    new_x, new_y = x + ch_x , y + ch_y
                    if inbound(new_x, new_y):
                        new_board = [list(current[0]) , list(current[1])]
                        new_board[new_x][new_y] , new_board[x][y] = new_board[x][y], new_board[new_x][new_y]
                        if (tuple(new_board[0]) , tuple(new_board[1])) not in visited:
                            queue.append((tuple(new_board[0]) , tuple(new_board[1])))
                            visited.add((tuple(new_board[0]) , tuple(new_board[1])))
                
            level += 1
            
        return -1
            
            
                        
                
                        
        
        