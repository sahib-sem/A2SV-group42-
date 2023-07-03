class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dp(i , robbed_last):
            
            if i == 0:
                if robbed_last:
                    return 0
                return nums[i]
            
            elif i == 1:
                if robbed_last:
                    return nums[1]
                else:
                    return max(nums[1] , nums[0])
                
            
            state = (i, robbed_last)
            if state not in memo:
                if not robbed_last and i == len(nums) - 1:
                    ans1 = nums[i] + dp(i - 2 , not robbed_last)
                else:
                    ans1 = nums[i] + dp(i - 2, robbed_last)
                    
                memo[state] = max(ans1 , dp(i - 1, robbed_last))
            
            return memo[state]
        
        return dp(len(nums) - 1 , False)
            
            
            
            
        
        
            
        