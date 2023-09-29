class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
    
        def dp(i, path_sum, memo = {}):
            
            if i == len(stones):
                if path_sum < 0:
                    return float('inf')
                return path_sum
            
            if (i, path_sum) in memo:
                return memo[(i, path_sum)]
            
            
            memo[(i, path_sum)] = min(dp(i + 1, path_sum + stones[i]), dp(i + 1, path_sum - stones[i]))
            
            return memo[(i, path_sum)]
        
        return dp(0, 0)
            