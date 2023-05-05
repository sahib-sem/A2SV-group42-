class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        
        graph = defaultdict(list)
        visited = set()
        queue = deque()
        if source == target:
            return 0
        for idx, route in enumerate(routes):
            
            for i in  range(len(route)):
                if route[i] == source:
                    queue.append(idx)
                    visited.add(idx)
                graph[route[i]].append(idx)
        
        bus = 1   
        while queue:
            
            length = len(queue)
            for _ in range(length):
                current = queue.popleft() # bus number 
                
                for nei in routes[current]:
                    if nei == target:
                        return bus
                
                    for new_node in graph[nei]:
                        if new_node not in visited:
                            queue.append(new_node)
                            visited.add(new_node)
            bus += 1
                        
                
                
        
        return -1
            
        
        
        
                
                
                