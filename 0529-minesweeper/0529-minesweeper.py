class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        x, y = click
        row = len(board)
        col = len(board[0])
        directions = [[1,0], [0, 1] , [-1, 0], [0, -1] , [1, 1], [-1, 1], [1, -1], [-1, -1]]
        def inbound(x, y):
            return 0 <= x < row and 0 <= y < col
        
            
        def dfs(x, y, board):
            
            stack = [(x, y)]
            
            while stack:
                
                curr_x, curr_y = stack.pop()
                count = 0
                temp = []
                for change_x , change_y in directions:
                    new_x, new_y = curr_x + change_x , curr_y + change_y
                    if inbound(new_x, new_y) and board[new_x][new_y] == 'M':
                        count += 1
                    if inbound(new_x , new_y) and board[new_x][new_y] == 'E':
                        temp.append((new_x, new_y))
                if count > 0:
                    board[curr_x][curr_y] = str(count)
                else:
                    board[curr_x][curr_y] = 'B'
                    stack.extend(temp)
            return board
                
        
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        if board[x][y] == 'E':
            return dfs(x, y, board)
        