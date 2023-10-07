class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        
        n = len(gas)
        
        for i in range(n):
            diff.append(gas[i] - cost[i])
        
        j = 0
        
        while j < n:
            
            if diff[j] >= 0:
                start = j
                summ = 0
                i = -1
                while start < n:
                    summ += diff[start]
                    
                    if summ < 0:
                        break
                    start += 1
                
                if start == n:
                    i = 0
                    while i < j:
                        summ += diff[i]
                        if summ < 0:
                            break
                        i += 1
                    if i == j:
                        return j
                if i != -1:
                    break
                
                j = start
            else:
                j += 1
                
        
        return -1
                    
                    
            
            
            
        
            
            
            
            
                