class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        parent = {node:set() for node in range(n)}
        graph = defaultdict(list)
        inDegree = [0 for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            inDegree[b] += 1
        
        queue = deque()
        
        for node, val in enumerate(inDegree):
            if val == 0:
                queue.append(node)
                
            
        while queue:
            
            current = queue.popleft()
            
            for nei in graph[current]:
                
                parent[nei] = parent[nei].union(set([current, *parent[current]]))
                inDegree[nei] -= 1
                
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        
        return [sorted(list(lst)) for lst in parent.values()]
            
        