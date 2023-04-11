class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            u, v = edge 
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(graph, curr, visited):
            if curr == destination:
                return True 
            
            visited.add(curr)
            
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    if dfs(graph, neighbour , visited):
                        return True
            return False
        
        return dfs(graph, source, set())
                
            
        