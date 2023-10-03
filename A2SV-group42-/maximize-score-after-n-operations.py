class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        
        '''
        
                2n
                
            n - pair of numbers
            
            
        
        '''
        
        def gcd(x, y):
            
            if y == 0:
                return x
            
            return gcd(y , x % y)
        
        
        target = len(nums) ** 2  - 1
        
        
        def backtrack(i, bits, memo = {}):
            nonlocal target
            
            if bits == target:
                return 0
            
            if (i, bits) in memo:
                return memo[(i, bits)]
            
            ans = 0
            for idx, num in enumerate(nums):
                
                if bits & (1 << idx) == 0:
                    
                    bits |= 1 << idx
                    
                    for j, num2 in enumerate(nums):

                        if bits & (1 << j) == 0:
                            
                            bits |= (1 << j)
                            
                            
                            
                            ans = max(ans, i * gcd(num, num2) + backtrack(i + 1, bits))
                            
                            
                            
                            bits = bits & ~(1 << j)
                            
                    bits = bits & ~(1 << idx)
            
            memo[(i, bits)] = ans
            return ans
            
            
        
        return backtrack(1, 0)
        

                            
        
        
        
        