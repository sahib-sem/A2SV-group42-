class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def count_primes(num):
            d = 2
            count = set()
            
            while d * d <= num:
                
                while num % d == 0:
                    count.add(d)
                    num //= d
                
                d += 1
            
            if num > 1:
                count.add(num)
            return count
        
        ans = set()
        for num in nums:
            set1 = count_primes(num)
            ans = ans.union(set1)
        
        return len(ans)
            
            
        