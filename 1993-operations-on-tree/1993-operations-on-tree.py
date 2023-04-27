class LockingTree:

    def __init__(self, parent: List[int]):
        self.locked = set()
        self.lock_map = {}
        self.graph = {i:[] for i in range(len(parent))}
        
        self.lst = []
        for i in range(len(parent)):
            if parent[i] != -1:
                self.graph[parent[i]].append(i)
        
    def checkAnsestor(self, root , target):
        if root in self.locked:
            return False
        if root == target:
            return True
            
        ans = False
        for child in self.graph[root]:
            res = self.checkAnsestor(child, target)
            ans |= res
        
        return ans 
    
    def checkDescendant(self, source, lst):
       
        if source in self.locked:
            self.lst.append(source)
        
        
        for neighbour in self.graph[source]:
            self.checkDescendant(neighbour, lst)
            

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked.add(num)
            self.lock_map[num] = user
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.lock_map.get(num, -1) == user:
            self.locked.discard(num)
            del self.lock_map[num]
            return True
        return False
            
        

    def upgrade(self, num: int, user: int) -> bool:
        
        if num in self.locked:
            return False
        self.lst = []
        self.checkDescendant(num, [])
        
        if len(self.lst) == 0:
            return False
        
        if self.checkAnsestor(0, num):
            self.lock_map[num] = user
            self.locked.add(num)
            
            for n in self.lst:
                self.locked.discard(n)
                if n in self.lock_map:
                    del self.lock_map[n]
            
            return True
        
        return False
        
        
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)