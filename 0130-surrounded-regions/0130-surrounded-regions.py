class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flipped_pos = []
        visited = set()
        directions = [[1, 0] , [-1, 0], [0, -1], [0, 1]]
        
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c <len(board[0])
        
        def dfs(r, c):
            nonlocal visited
            
            stack = [(r, c)]
            visited.add((r, c))
            temp = [(r, c)]
            surrounded = False
            while stack:
                x, y = stack.pop()
                
                for ch_x , ch_y in directions:
                    new_x , new_y = x + ch_x , y + ch_y
                    
                    if inbound(new_x, new_y) and board[new_x][new_y] == 'O' and (new_x, new_y) not in visited:
                        
                        stack.append((new_x , new_y))
                        if not surrounded:
                            temp.append((new_x , new_y))
                        visited.add((new_x , new_y))
                    
                    elif not inbound(new_x , new_y):
                        surrounded = True
            if not surrounded:
                return [True , temp]
            else:
                return [False , []]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    res = dfs(r, c)
                    if res[0]:
                        flipped_pos.extend(res[1])
        for x, y in flipped_pos:
            board[x][y] = 'X'