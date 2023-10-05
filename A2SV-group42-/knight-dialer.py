class Solution:
    def knightDialer(self, n: int) -> int:
        
        knightDirection = [(2, 1), 
                           (2, -1),
                           (-2, 1), 
                           (-2, -1),
                            (1, 2),
                           (-1, 2),
                           (1, -2),
                           (-1, -2)
                          ]
        
        mod = 10**9 + 7
        def inbound(r, c):
            
            res = 0 <= r < 4 and 0 <= c < 3 
            res2 = (r == 3 and c == 0  or r == 3 and c == 2)
            
            return res and not res2
        def dp(curr, jumps, memo):
            
            if jumps == 1:
                
                return 1
            
            if (curr, jumps) in memo:
                return memo[(curr, jumps)]
            
            r, c = curr
            
            ans = 0
            
            for x, y in knightDirection:
                
                new_x, new_y = x + r , y + c
                
                if inbound(new_x, new_y):
                    
                    ans += dp((new_x, new_y), jumps - 1, memo)
            
            memo[(curr, jumps)] = ans
                    
            return ans
        
        memo = {}
        ans = 0
        for i in range(3):
            
            for j in range(3):
                
                ans += dp((i, j), n, memo)
        
        ans += dp((3, 1), n, memo)
        
        return ans % mod
                    
            
            
            
            