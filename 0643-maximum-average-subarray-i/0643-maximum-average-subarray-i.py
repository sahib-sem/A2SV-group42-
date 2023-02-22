class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        curr = 0
        start = 0
        for end in range(len(nums)):
            curr += nums[end]
            if end-start+1 >= k:
                max_sum = max(max_sum,curr)
                curr -= nums[start]
                start += 1
        return max_sum / k
            
        
        