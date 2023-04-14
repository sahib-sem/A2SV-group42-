class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        arr = [0 for i in range(len(graph))] # colors array
        
        for node in range(len(graph)):
            
            arr[node] = 1
            stack = [node]
            
            while stack:
                
                current = stack.pop()
                
                for neighbour in graph[current]:
                    
                    
                    if not arr[neighbour]:
                        arr[neighbour] = -1 * arr[current]
                        stack.append(neighbour)
                    elif arr[neighbour] == arr[current]:
                        return False
                        
                        
            
            arr = [0 for _ in range(len(graph))]
            
        return True