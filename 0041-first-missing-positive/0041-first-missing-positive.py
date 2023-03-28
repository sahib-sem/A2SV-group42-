class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            swap = nums[i] - 1
            if 0 < nums[i] < len(nums) + 1 and nums[i] != i + 1 and nums[swap] != nums[i]:
                nums[i] , nums[swap] = nums[swap] , nums[i]
            else:
                i += 1
       
        for k in range(len(nums)):
            if nums[k] != k + 1:
                return k+ 1
        
        return len(nums) + 1
            
        