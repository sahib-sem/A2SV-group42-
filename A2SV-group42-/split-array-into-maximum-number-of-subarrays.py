class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        minimum = (1 << 20 ) - 1
        
        for i in range(len(nums)):
            
            minimum = minimum & nums[i]
        
        if minimum != 0:
            return 1
        
        else:
            
            i = 0
            current = (1 << 20 ) - 1
            ans = 0
            
            while i < len(nums):
                
                
                current = current & nums[i]
               
                if current == 0:
                    ans += 1
                    
                    current = (1 << 20 ) - 1
                
                
            
                i += 1
                
            return ans
                
        