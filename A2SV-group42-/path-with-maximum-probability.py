class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # weighted graph 
        # kind of similar to shortest path 
        
        # 0 -> 2     0 -> 1 -> 2   or 0 -> 2
        
        graph = defaultdict(list)
        
        for idx, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[idx]))
            graph[b].append((a, succProb[idx]))
        
        
        heap = [(-1, start_node)]
        visited = set()
        
        while heap:
            
            prop , node = heapq.heappop(heap)
            
            if node == end_node:
                
                return -prop
            
            if node in visited:
                continue
                
            visited.add(node)
            
            for nei , succP in graph[node]:
                
                heapq.heappush(heap, (prop * succP, nei))
        
        
        return 0
            
        
        
        
        
        
        