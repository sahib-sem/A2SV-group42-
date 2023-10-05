class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n, m = len(nums1), len(nums2)
        
        def dp(i, j, memo = {}):
            
            nonlocal n, m
            
            if i == n or j == m:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if nums1[i] == nums2[j]:
                memo[(i, j)] = 1 + dp(i + 1, j + 1, memo)
            
            else:
                memo[(i, j)] = max(dp(i + 1, j) , dp(i , j + 1))
            
            return memo[(i, j)]
        
        return dp(0, 0)