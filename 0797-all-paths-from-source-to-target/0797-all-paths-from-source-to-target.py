class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        ds = len(graph) - 1
        
        def dfs(curr, temp):
            temp.append(curr)
            
            if curr == ds:
                paths.append(temp[:])
                
            for neighbour in graph[curr]:
                dfs(neighbour , temp)
            
            temp.pop()
        
        dfs(0, [])
        
        return paths
            