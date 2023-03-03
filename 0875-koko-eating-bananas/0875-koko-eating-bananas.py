class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def findHours(piles , k):
           
            count = 0
            for banana in piles:
                if banana <= k:
                    count += 1
                else:
                    temp = math.ceil(banana / k)
                    count += temp
                    
            return count 
        
        low = 0
        high = max(piles) + 1
        
        while high > low + 1:
            
            mid = low + (high - low) // 2
            
            if findHours(piles , mid) <= h:
                high = mid
            else:
                low = mid
        return high
            
        