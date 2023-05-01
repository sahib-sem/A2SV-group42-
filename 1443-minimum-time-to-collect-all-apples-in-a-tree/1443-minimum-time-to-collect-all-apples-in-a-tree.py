class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # do a dfs and calculate the shortest path from the root to each node 
        
        graph = defaultdict(list)
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            
        def dfs(current_node , visited):
            if len(graph[current_node]) == 1 and current_node != 0:
                return int(hasApple[current_node])
            
            visited.add(current_node)
            res = 0
            for nei in graph[current_node]:
                if nei not in visited:
                    
                    res += dfs(nei, visited)
            
            if current_node != 0:
                if res > 0:
                    return res + 1
                else:
                    
                    return int(hasApple[current_node])
            return res 
       
        return 2 * dfs(0 , set())
            
            
        