class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        
        # place the heaters to their closest house 
        
        if houses == heaters:
            return 0
        i = 0
        j = 0
        raduis = 0
        houses.sort()
        heaters.sort()
        
        while i < len(houses) and j < len(heaters):
            
            house = houses[i]
            
            while j < len(heaters) - 1 and abs(heaters[j + 1] - house) < abs(heaters[j]- house):
                
                j += 1
               
            raduis = max(raduis, abs(heaters[j] - house))
            
            i += 1
        
        return raduis 
            
        
        
                
                
                
        
        
                
            
            