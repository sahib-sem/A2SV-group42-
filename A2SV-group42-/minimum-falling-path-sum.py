class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        for r in range(n - 2, -1 , -1):
            for c in range(n):
                ans1, ans2 , ans3 = float('inf'), matrix[r + 1][c] , float('inf')
                
                if c - 1 >= 0:
                    ans1 = matrix[r + 1][c - 1]
                if c + 1 < n:
                    ans3 = matrix[r + 1][c + 1]
                
                ans = min(ans1, ans2, ans3)
                matrix[r][c] += ans
        
        return min(matrix[0])
            
            
            
        
        
        