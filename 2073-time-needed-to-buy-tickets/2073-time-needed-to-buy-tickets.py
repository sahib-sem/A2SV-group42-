class Solution:  
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time_taken = 0
        target = tickets[k]
        
        for i in range(len(tickets)):
            
            if k < i and tickets[i] >= target:
                time_taken += target - 1
            elif tickets[i] < target:
                time_taken += tickets[i]
            else:
                time_taken += target 
        return time_taken 