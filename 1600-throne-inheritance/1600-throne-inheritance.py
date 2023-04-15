class ThroneInheritance:
    '''
           king
        
        andy   bob    catherine
     matthew    alex  asha   
    '''

    def __init__(self, kingName: str):
        
        self.graph = {kingName: []}
        self.king = kingName
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        self.graph[childName] = []
        

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.king]
        inheritance = []
        
        while stack:
            
            current = stack.pop()
            if current not in self.dead:
                    inheritance.append(current)
            temp = []
            for child in self.graph[current]:
                temp.append(child)
                
            temp = temp[::-1]
            stack.extend(temp)
        
        return inheritance
            
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()