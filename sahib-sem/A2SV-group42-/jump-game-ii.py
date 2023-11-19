class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        # greedy 
        memo = {}
        
        def dp(i):
            if i >= len(nums) - 1:
                return 0
            
            if nums[i] == 0:
                return float('inf')
            
            ans = float('inf')
            
            if i not in memo:
                for j in range(1, min(nums[i] + 1 , len(nums))):
                    
                    ans = min(ans, 1 + dp(i + j))
                
                memo[i] = ans
            
            return memo[i]
        
        return dp(0)
            