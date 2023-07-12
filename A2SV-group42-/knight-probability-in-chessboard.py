class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # [0, 0, 0]
        # [0, 0, 0]
        # [0, 0, 0]
        memo = {}
        directions = [
            (2, 1),
            (2, -1), 
            (-2 , 1), 
            (-2 , -1),
            (1, 2), 
            (-1, 2), 
            (1, -2), 
            (-1, -2)
        ]
        
        def dp( r , c , curr):
            if curr == k:
                if 0 <= r < n and 0 <= c < n:
                    return 1
                else:
                    return 0
            
            if not (0 <= r < n and 0 <= c < n):
                return 0
            
            state = (r, c, curr)
            ans = 0 
            
            if state not in memo:
                for x, y in directions:
                    ans += dp(r + x, c + y , curr + 1)
                
                memo[state] = ans
            
            return memo[state]
        
        return dp(row, column, 0) / (8 ** k)
                
                
            