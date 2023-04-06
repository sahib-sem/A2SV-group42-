class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # if a num exists in every edge list return that
        i = 0
        if len(edges) == 1:
            return edges[0]
        
        look_for = set(edges[0]).intersection(set(edges[1])).pop()
            
        
        return look_for
            
        