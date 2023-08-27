class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        destination = n ** 2
        
        dic = {}
        start = destination
        reverse = True if n % 2 == 0 else False
        
        for r in range(n):
            if reverse:
                for c in range(n):
                    dic[start] = (r, c)
                    start -= 1
            else:
                for c in range(n - 1, -1 , -1):
                    dic[start] = (r, c)
                    start -= 1
            
            reverse = not reverse
                    
            
        queue = deque([(1, False, 0)])
        visited = {}
        visited[1] = 0
        ans = []
        
        while queue:
            
            length = len(queue)
            
            for _ in range(length):
                
                current, prev_ladder_snake, level = queue.popleft()
                
                if current == destination:
                    ans.append(level)

                r, c = dic[current]
                
                if board[r][c] != -1 and not prev_ladder_snake:
                    queue.append((board[r][c], True, level))
                    continue
                
                for nei in range(current + 1, min(current + 6 , destination ) + 1):
                    
                    if nei not in visited or visited[nei] > level:
                        
                        queue.append((nei, False, level + 1))
                        visited[nei] = level
           
        
        
        if len(ans) > 0:
            return min(ans)
        
        return -1
                
        
        