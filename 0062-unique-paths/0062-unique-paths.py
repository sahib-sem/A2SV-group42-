class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(r,c, ans):
            if r < 0 or r >= m or c <0 or c>= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) not in memo:
                memo[(r,c)] = dp(r + 1, c, ans) + dp(r, c + 1, ans)
            ans += memo[(r,c)]
            
            return ans
        
        return dp(0, 0, 0)
        