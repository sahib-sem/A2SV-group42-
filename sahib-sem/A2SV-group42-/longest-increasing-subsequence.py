class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        dp = {}
        
        for i in range(len(nums)):
            
            max_sub = 0
            
            for key, val in dp.items():
                
                if nums[i] > nums[key]:
                    
                    max_sub = max(max_sub, val)
            
            dp[i] = max_sub + 1
        
        return max(dp.values())
        