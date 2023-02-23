class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prefix_product = 1
        suffix_product = 1
        
        
        for i in range(1,len(nums)):
            prefix_product *= nums[i-1]
            prefix[i] = prefix_product
        
        for j in range(len(nums)-2,-1,-1):
            suffix_product *= nums[j+1]
            suffix[j] = suffix_product
        
        for i in range(len(suffix)):
            prefix[i] *= suffix[i]
        
        return prefix
            
            
        
        
        