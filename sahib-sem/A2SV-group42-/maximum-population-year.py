class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        prefix = [0] * 101 
        
        for b, d in logs:
            prefix[b - 1950] += 1
            prefix[d - 1950] -= 1
        
        prefix = list(accumulate(prefix))
        
        maxx = max(prefix)
        
        
        for i in range(101):
            
            if prefix[i] == maxx:
                
                return 1950 + i
        