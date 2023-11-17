# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        l = 1
        
        h = mountain_arr.length() - 2
        peak = -1
        
        while h >= l:
            
            mid = l + (h - l) // 2
            
            before_mid = mountain_arr.get(mid - 1)
            at_mid = mountain_arr.get(mid)
            after_mid = mountain_arr.get(mid + 1)
            
            if before_mid <at_mid > after_mid:
                peak = mid
                break
            
            elif before_mid < at_mid:
                l = mid + 1
            
            else:
                h = mid - 1
            
        
        l = 0
        h = peak
        
        
        while h >= l:
            
            mid = l + (h - l) // 2
            
            at_mid = mountain_arr.get(mid)
            
            
            
            if at_mid == target:
                return mid
            
            elif at_mid < target:
                l = mid + 1
            else:
                
                h = mid - 1
        
        l = peak 
        h = mountain_arr.length() - 1
        
        
        
        while h >= l:
            
            mid = l + (h - l) // 2
            
            at_mid = mountain_arr.get(mid)
            
            if at_mid == target:
                return mid
            
            elif at_mid > target:
                l = mid + 1
                
            else:
                h = mid - 1
                
        
        return -1
            
                    
                    
                    
        
        