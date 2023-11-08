class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    
        graph = defaultdict(list)
        
        for idx, (a, b) in enumerate(equations):
            
            graph[a].append((b, values[idx]))
            graph[b].append((a , 1 / values[idx]))
            
        def dfs(start, target):
            
            stack = [(start, 1)]
            visited = set({})
            
            while stack:
                
                
                curr , ans = stack.pop()
            
                
                if curr == target and graph[curr]:
                    
                    return ans
                
                if curr in visited:
                    continue
                
                visited.add(curr)
                
                for nei, val in graph[curr]:
                    
                    if curr == start:
                        stack.append((nei, val))
                    else:
                        stack.append((nei, ans * val))
            
            return -1
        
        ans = []
        for a, b in queries:
            
            ans.append(dfs(a, b))
            
        
        return ans
        
        
                    
        
        