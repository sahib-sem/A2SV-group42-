class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        inDegree = [0 for _ in range(len(quiet))]
        ans = [i for i in range(len(quiet))]
        graph = defaultdict(list)
        
        for a, b in richer:
            graph[a].append(b)
            inDegree[b] += 1
        
        queue = deque()
        
        for idx, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(idx)
        
        
        while queue:
            
            current = queue.popleft()
            
            for nei in graph[current]:
                inDegree[nei] -= 1

                if quiet[ans[current]] < quiet[ans[nei]]:
                    ans[nei] = ans[current]
                if inDegree[nei] == 0:
                    queue.append(nei)
            
        return ans
            
        
        
        