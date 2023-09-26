class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
         30 -> 0
         10 -> 0
         1 -> 5
         -10 -> 11
         -5 -> 6 
         3 -> 2
         -3 -> 5
         -2 -> 7
        '''
        
        m , n = len(dungeon) , len(dungeon[0])
        
        end = dungeon[m - 1][n - 1]
        
        if end > 0:
            dungeon[m - 1][n - 1] = 1
        
        else:
            dungeon[m - 1][n - 1] = (1 - end)
        

        for r in range(m - 1, -1 , -1):
            
            for c in range(n - 1, -1, -1):
                
                if r == m - 1 and c == n - 1:
                    continue
                
                ans1 , ans2 = float('inf'), float('inf')
                if c + 1 < n:
                    ans1 = dungeon[r][c + 1]
                
                if r + 1 < m:
                    ans2 = dungeon[r + 1][c]
                
                provide = min(ans1, ans2)
                if dungeon[r][c] >= provide:
                    dungeon[r][c] = 1
                else:
                    dungeon[r][c] = (provide - dungeon[r][c])

        
        return dungeon[0][0]
                    
                
            
        