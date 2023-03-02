class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # optimized 
        prefix_sum = {0:1}
        ans = 0
        summ = 0
        n = len(nums)
        
        for i in range(n):
            
            summ += nums[i]
            ans += prefix_sum.get(summ - goal , 0)
            prefix_sum[summ] = prefix_sum.get(summ , 0) + 1
        
        return ans
            
            