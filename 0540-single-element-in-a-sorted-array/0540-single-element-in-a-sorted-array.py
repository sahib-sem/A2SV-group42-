class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        while high >= low:
            
            mid = (low + high) // 2
            
            
            #out of bound conditions
            
            if nums[mid] == nums[mid + 1]:
                
                if (high - mid) % 2 == 0:
                    low = mid + 2
                    
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if (mid - low) % 2 == 0:
                    high = mid - 2
                    
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[mid]
        
                
                    
                    