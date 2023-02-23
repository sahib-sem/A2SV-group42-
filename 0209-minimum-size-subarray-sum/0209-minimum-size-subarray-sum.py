class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        curr = 0
        min_length = len(nums) + 1
        for end in range(len(nums)):
            curr += nums[end]
            while curr - nums[start] >= target:
                curr -= nums[start]
                start += 1
            if curr >= target:
                min_length = min(min_length , end - start + 1)
        if min_length == len(nums) + 1:
            return 0
        else:
            return min_length
            
        