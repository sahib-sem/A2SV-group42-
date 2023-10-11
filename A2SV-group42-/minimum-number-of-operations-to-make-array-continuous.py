class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        j = 0
        i = 0
        n = len(nums)
        
        ans = n
        nums = sorted(set(nums))
        
        while i < len(nums):
            
            while j < len(nums) and nums[j] < nums[i] + n:
                j += 1
            
            ans = min(ans, n - (j - i))
            
            i += 1
        
        return ans
        
        
        
        