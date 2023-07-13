class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        ans = 0
        for difference in range(-500, 501):
            dp = defaultdict(int)
            
            for i in range(len(nums)):
                num = nums[i]
                
                dp[num] = dp[num - difference] + 1
            
            ans = max(ans, max(dp.values()))

        return ans