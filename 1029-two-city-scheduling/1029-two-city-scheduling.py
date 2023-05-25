class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lst = []
        for idx , (a, b) in enumerate(costs):
            lst.append((a - b ,a, b))
        
        lst.sort()
        i , j = 0, len(costs) - 1
        cost = 0
                       
        while i < j:
            cost += lst[i][1]
            cost += lst[j][2]
            i += 1
            j -= 1
                       
        return cost
                       
                       
                       
                       
                    
        
        
        
        
            
        