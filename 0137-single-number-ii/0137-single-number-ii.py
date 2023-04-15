class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        j = -2
        
        for i in range(32):
            ones = 0
            for num in nums:
                if num & (1<<i) == (1<<i):
                    ones += 1
                    
                    
            if ones % 3:
                ans |= 1 << i
               
        
        
        return ans if ans < (1 << 31) else ans - (1 << 32)
            