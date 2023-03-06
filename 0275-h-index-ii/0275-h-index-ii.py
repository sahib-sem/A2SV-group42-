class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def countCitation(arr , h):
            count = 0
            for num in arr:
                if num >= h:
                    count += 1
            return count
        
        low = -1
        high = max(citations) + 1
        
        while high > low + 1:
            
            mid = low + (high - low) // 2
            
            if countCitation(citations , mid) >= mid:
                low = mid
            else:
                high = mid
                
                
        return low
            
            
        
        