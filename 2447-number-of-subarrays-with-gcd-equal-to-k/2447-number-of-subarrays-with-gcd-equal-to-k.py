class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        count = 0
        for i in range(len(nums)):
            total = nums[i]
            for j in range(i, len(nums)):
                j = nums[j]
                total = gcd(total , j)
                if total == k:
                    count += 1
        return count 
                    
                
        
        