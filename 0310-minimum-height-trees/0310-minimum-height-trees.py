class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = [0 for _ in range(n)]
        
        for a, b in edges:
            
            graph[a].append(b)
            graph[b].append(a)
            
            inDegree[a] += 1
            inDegree[b] += 1
        
        queue = deque()
        visited = set()
        ans = []
        for idx , ind in enumerate(inDegree):
            if ind == 1:
                queue.append(idx)
            ans.append(idx)
        
        while queue:
            
            length = len(queue)
            best = ans
            ans = []
            for _ in range(length):
                
                current = queue.popleft()
                
                for nei in graph[current]:
                    if nei not in visited:
                        inDegree[nei] -= 1
                        if inDegree[nei] == 1:
                            queue.append(nei)
                            visited.add(nei)
                            ans.append(nei)
            if ans == []:
                ans = best
                            
        return ans
                
                            
            
            
        
        
                
            
        
        
        