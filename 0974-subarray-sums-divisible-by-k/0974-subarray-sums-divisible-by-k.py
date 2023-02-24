class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        curr = 0
        res = 0
        
        for end in range(len(nums)):
            curr += nums[end]
            m = curr % k
            res += prefix.get(m , 0)
            prefix[m] = prefix.get(m,0) + 1
        return res
            
            
        
    