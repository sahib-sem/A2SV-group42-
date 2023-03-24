class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append(-1)
        # use cyclic sort
        
        i = 0
        while i < len(nums):
            if i != nums[i] and nums[i] != - 1:
                idx = nums[i]
                nums[i] , nums[idx] = nums[idx] ,nums[i]
            else:
                i += 1
        
        return nums.index(-1)
                