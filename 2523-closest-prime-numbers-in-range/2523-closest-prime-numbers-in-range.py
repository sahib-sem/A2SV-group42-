class Solution:
    def check_prime(self, num):
        if num <= 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
                
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        best = [None , None]
        first = seconde =  None
        for i in range(left, right + 1):
            if best[0] == 1 or best[0] == 2:
                break
            if self.check_prime(i):
                if not first:
                    first = i
                else:
                    second = i
                    
                    if not best[0]:
                        best = [second - first , [first, second]]
                    else:
                        if second - first < best[0]:
                            best = [second - first , [first, second]]
                    first = second
        if not best[0]:
            return [-1, -1]
        else:
            return best[-1]
                
        
        
        