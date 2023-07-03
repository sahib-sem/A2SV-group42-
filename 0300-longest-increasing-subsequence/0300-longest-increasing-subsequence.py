class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
       
        memo = {}
        
        for num in nums:
            
            max_ele = 0
            for key , val in memo.items():
                if num > key:
                    max_ele = max(max_ele, val)
            
            memo[num] = max_ele + 1
        
        return max(memo.values())
        
                
            
            
            
            
        
        
            
            
        
        