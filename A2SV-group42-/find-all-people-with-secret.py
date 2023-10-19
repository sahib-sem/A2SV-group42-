class UnionFind:
    
    def __init__(self, people):
        
        self.connection = {}
        self.rank = {}
        for a, b in people:
            self.connection[a] = a
            self.connection[b] = b
            self.rank[a] = 1
            self.rank[b] = 1
        
    def find(self, x):
        
        if x == self.connection[x]:
            return x
        
        self.connection[x] = self.find(self.connection[x])
        return self.connection[x]
    
    def union(self, x, y):
        
        repX = self.find(x)
        repY = self.find(y)
        
        if repX != repY:
            
            if self.rank[repX] > self.rank[repY]:
                
                self.connection[repY] = repX
                
            elif self.rank[repX] < self.rank[repY]:
                
                self.connection[repX] = repY 
            else:
                self.connection[repY] = repX
                self.rank[repX] += 1
                
    def findConnection(self, x):
        
        ans = set()
        
        rep = self.find(x)
        for n in self.connection:
            
            if rep == self.find(n):
                ans.add(n)
        
        return ans
         
        
        
        


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    
        people_meeting_time = defaultdict(list)
        
        people_with_secret = set({0, firstPerson})
        
        for x, y, t in meetings:
            
            people_meeting_time[t].append((x, y))
            
            
        
        # sort the dictionary based on meeting time
        
        people_meeting_time = dict(sorted(people_meeting_time.items() , key = lambda x:x[0]))
        
        for people in people_meeting_time.values():
            
            uf = UnionFind(people)
            
            
            secrets = set()
            for x, y in people:
                
                uf.union(x, y)
                if x in people_with_secret:
                    secrets.add(x)
                if y in people_with_secret:
                    secrets.add(y)
            
            for p in secrets:
                
                if p in people_with_secret:
                    people_with_secret |= uf.findConnection(p)
                
            
                
            
            
            
            
        
        return people_with_secret
            
                
                    
        
        
        
        
        
        
        
        
        
        
        
        