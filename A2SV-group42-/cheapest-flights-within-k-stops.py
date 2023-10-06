class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for u, v, cost in flights:
            graph[u].append((v, cost))
    
        heap = [(-1 ,0, src)]
        heapq.heapify(heap)
        minimum = float('inf')
        visited = set()

        while heap:
            
            stop, dist, node  = heappop(heap)
            
            if node == dst:
                minimum = min(minimum , dist)
                        
            if (node, stop) in visited:
                continue
            
            visited.add((node, stop))
            

            for nbr, wgt in graph[node]:
                
                if stop < k:
                  
                    heapq.heappush(heap, (stop + 1 ,dist + wgt, nbr))
                

        return minimum if minimum != float('inf') else -1
        