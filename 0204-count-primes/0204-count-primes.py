class Solution:
    def countPrimes(self, n: int) -> int:
        
        def seive(n):
            arr = [True for _ in range(n + 1)]
            arr[0] = arr[1] = False
            
            i = 2
            up_to = math.ceil(math.sqrt(n))
            while i <= up_to:
                
                if arr[i]:
                    
                    j = i * i
                    
                    while j <= n:
                        arr[j] = False
                        j += i
                i += 1
            
            return arr
        res = []
        if n >2:
            res = seive(n)
        count = 0
        for i  in range(len(res) - 1):
            if res[i]:
                count += 1
        
        
        return count 