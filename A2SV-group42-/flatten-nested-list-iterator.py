# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.flattened = []
        
        for element in nestedList:
            self.flattened += self.flatter(element)
        self.N = len(self.flattened)
        self.i = 0
        
        
        
    
    def next(self) -> int:
        
        ans = self.flattened[self.i]
        self.i += 1
        
        return ans
        
    
    def hasNext(self) -> bool:
        
        return self.i < self.N
         
    def flatter(self, nestedList):
        
        if nestedList.isInteger():
            return [nestedList.getInteger()]
        
        ans = []
        
        for element in nestedList.getList():
            
            ans.extend(self.flatter(element))
        
        
        return ans
            
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())