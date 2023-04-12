class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ds = len(graph) - 1
        stack = [[0,0]]
        paths = []
        
        while stack:
            
            current , neighbour = stack[-1]
            
            if current == ds and neighbour == 0:
                paths.append(list(map(lambda x: x[0] , stack)))
            
            if neighbour < len(graph[current]):
                stack[-1][1] += 1
                stack.append([graph[current][neighbour] , 0])
            else:
                stack.pop()
        
        return paths