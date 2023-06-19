class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        last_first_ele = float('inf')
        for i in range(len(nums)):
            
            if nums[i] >= last_first_ele:
                continue
                
            last_first_ele = nums[i]
            first = nums[i]
            second = None
            j = i + 1
            
            while j < len(nums):
                
                if nums[j] > first:
                    if second != None:
                        if nums[j] > second:
                            return True
                        else:
                            second = nums[j]
                    else:
                        second = nums[j]
                    
                    
                j += 1
                
        
        return False
            
                    
                
                
                
                
                
        
        
            