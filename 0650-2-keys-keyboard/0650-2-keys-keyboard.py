class Solution:
    def minSteps(self, n: int) -> int:
        # do the prime factorization then then add those
        prime = 2
        lst = []
        while n > 1:
            
            while n % prime == 0:
                lst.append(prime)
                n //= prime
                
            prime += 1
        
        return sum(lst)
        
        
        