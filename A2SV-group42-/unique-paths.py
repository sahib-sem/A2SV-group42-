class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        total = m - 1 + n - 1
        
        # 2 + 6 = 8! 8 * 7 // 
        return factorial(total) // (factorial(m - 1) * factorial(n - 1))