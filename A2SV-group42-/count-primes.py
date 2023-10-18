class Solution:
    def countPrimes(self, n: int) -> int:
        
        
        def seive_erastotes(n : int):
            
            primes = [True] * n
            
            primes[0] = primes[1] = False
            
            i = 0
            
            while i < ceil(sqrt(n)):
                
                if primes[i]:
                    
                    j = i * i
                    
                    while j < n:
                        primes[j] = False
                        j += i
                
                i += 1
            
            return primes
        
        if n <= 2:
            return 0
        
        return seive_erastotes(n).count(True)
                
                
                
            
            