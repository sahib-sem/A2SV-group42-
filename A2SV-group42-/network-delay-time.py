class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        shortest_path = {node: float('inf') for node in range(1, n + 1)}
        
        for a , b, time in times:
            
            graph[a].append((b, time))
        
        min_heap = [(0, k)]
        heapq.heapify(min_heap)
       
        while len(min_heap) > 0:
            
            time_cost , curr_node = heapq.heappop(min_heap)
            
            if shortest_path[curr_node] <= time_cost:
                continue
            
           
            shortest_path[curr_node] = time_cost
            
            for child, time in graph[curr_node]:
                
                cost = time_cost + time
                heapq.heappush(min_heap, (cost, child))
        
        
  
        res = max(shortest_path.values())
        
        return res if res != float('inf') else -1
            
            
        
        