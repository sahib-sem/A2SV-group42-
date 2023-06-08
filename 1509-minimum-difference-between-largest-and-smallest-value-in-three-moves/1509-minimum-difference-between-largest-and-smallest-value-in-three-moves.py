class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        possible_sum = []
        if len(nums) <= 4:
            return 0
        
        j = -4 
        i = 0 
        
        while j != 0:
            
            pos1 = nums[j] - nums[i]
            
            possible_sum.append(pos1)
            
            j += 1
            i += 1
        
        print(possible_sum)
        
        return min(possible_sum)
        
    
      
                
                
        
        