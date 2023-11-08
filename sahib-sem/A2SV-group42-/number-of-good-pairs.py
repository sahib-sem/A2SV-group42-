class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # 3 = 3 
        # a a a a 
        # a a a
        # 2 1 
        # 1 + ... + n - 1
        # n * (n + 1) / 2
        # n - 1 * n / 2
        
        cnt = Counter(nums)
        
        ans = 0
        
        for val in cnt.values():
            
            ans += (val)*(val - 1) // 2
        
        return ans