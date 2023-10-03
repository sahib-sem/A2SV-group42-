class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs_array = [[a - b, a, b] for i , (a, b) in enumerate(costs)]
        costs_array.sort()
        cost = 0
        i , j = 0, len(costs_array) - 1
        
        while j > i:
            
            cost += costs_array[i][1]
            cost += costs_array[j][2]
            i += 1
            j -= 1
            
        return cost 
            
            
            
        