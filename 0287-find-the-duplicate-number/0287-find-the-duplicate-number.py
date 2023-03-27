class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = -1
        high = len(nums) + 1
        
        while high >  low + 1:
            mid = low + (high - low) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count <= mid:
                low = mid
            else:
                high = mid
        return high
        
                
            
        