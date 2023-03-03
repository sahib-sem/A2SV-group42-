class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while high >= low:
            
            mid = (low + high) // 2
            num_day = 0
            running_sum = 0
            
            for weight in weights:
                running_sum += weight
                if running_sum >= mid:
                    if running_sum > mid:
                        running_sum = weight
                    else:
                        running_sum = 0
                    num_day += 1
            if running_sum > 0:
                num_day += 1
                  
            
            if num_day > days:
                low = mid + 1
                
            else:
                
                high = mid - 1
        
        return low
            
                
        