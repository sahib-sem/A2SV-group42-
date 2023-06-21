class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.ans = 0
        memo = {}
        
        def dp(i,curr_sum):
            
            if i == len(nums):
                if curr_sum == target:
                    return 1
                return 0

            if (i + 1, curr_sum + nums[i]) not in memo:
                memo[(i + 1, curr_sum + nums[i])] = dp(i + 1, curr_sum + nums[i])
            if not (i + 1, curr_sum - nums[i]) in memo:
                memo[(i + 1, curr_sum - nums[i])] = dp(i + 1, curr_sum - nums[i])
                
            return memo[(i + 1, curr_sum + nums[i])] + memo[(i + 1, curr_sum - nums[i])]
        
        
        return dp(0,0)
        