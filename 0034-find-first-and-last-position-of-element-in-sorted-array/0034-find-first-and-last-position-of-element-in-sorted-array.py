class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(nums) - 1
        found = False
        
        # for the first occurence        
        while high >= low:
            
            mid = (low + high) // 2
            
            if nums[mid] > target:
                high = mid - 1
                
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                found = True
                
        first_occurence = low if found else -1
        low = 0
        high = len(nums) - 1
        found = False
        
        # for the second occurence        
        while high >= low:
            
            mid = (low + high) // 2
            
            if nums[mid] > target:
                high = mid - 1
                
            elif nums[mid] < target:
                low = mid + 1
            else:
                low = mid + 1 
                found = True
                
        second_occurence = high if found else - 1
        
        return [first_occurence , second_occurence]
        
                
                
            
        