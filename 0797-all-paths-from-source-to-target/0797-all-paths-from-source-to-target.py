class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ds = len(graph) - 1
        paths = []
        stack = [[0, 0]]#rrent, last_neibour 
        
        while stack:
            current, nei = stack[-1]
            if current == ds and nei == 0:
                paths.append(list(map(lambda x: x[0], stack)))
                            
            if nei < len(graph[current]):
                stack[-1][1] += 1
                stack.append([graph[current][nei], 0])
            else:
                stack.pop()
            
    
        return paths 
                