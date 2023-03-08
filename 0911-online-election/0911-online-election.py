class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons = persons
        self.times = times 
        winner_mapping = {}
        winner = {}
        current_winner = self.persons[0]
        maxx = 0
        
        for idx , person in enumerate(self.persons):
            
            winner_mapping[person] =  winner_mapping.get(person , 0) + 1
            if winner_mapping[person] >= maxx:
                maxx = winner_mapping[person]
                current_winner = person
                
            winner[idx] = current_winner
            
        self.winner = winner
            
        
        
    def insertIndex(self, time):
        low = - 1
        high = len(self.times)
        
        while high > low + 1:
            mid = low + (high - low) // 2
            
            if self.times[mid] < time:
                low = mid
            else:
                high = mid
                
        return high
    
    def q(self, t: int) -> int:
        
        idx = self.insertIndex(t)
        
        if idx >= len(self.times):
            return self.winner[idx - 1]
        if t < self.times[idx]:
            return self.winner[idx - 1]
        
        return self.winner[idx]

        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)