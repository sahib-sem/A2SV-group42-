class RandomizedSet:

    def __init__(self):
        
        self.num_index = defaultdict(int)
        self.elements = []
        

    def insert(self, val: int) -> bool:
        if val not in self.num_index:
            self.elements.append(val)
            self.num_index[val] = len(self.elements) - 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        
        if val in self.num_index:
            last = self.elements[-1]
            last_idx = len(self.elements) - 1
            val_idx = self.num_index[val]
            
            self.elements[last_idx] , self.elements[val_idx] = self.elements[val_idx] , self.elements[last_idx]
            self.num_index[last] = val_idx
            self.elements.pop()
            del self.num_index[val]
            
            return True
        
        
        return False

    def getRandom(self) -> int:
        
        idx = random.randint(0, len(self.elements) - 1)
        
        return self.elements[idx]
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()