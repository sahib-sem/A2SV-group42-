class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # {0:[1, 2] ,1: [] , 2:[3] , 3:[4]}
        # let's assume we have n bombs numbered from 0 to n -1
        # let's build a graph the vertices will be the bombs and the bombs each of them
        # can detonate will be their neighbour
        
        # to build the graph O(N ** 2)
        graph = defaultdict(list)
        def euclidean_distance(x, y, x1, y1):
            delta_x = abs(x - x1)
            delta_y = abs(y - y1)
            
            return math.sqrt(delta_x ** 2 + delta_y ** 2)
        for node , attribute in enumerate(bombs):
            x, y , r = attribute
            
            for node1 , attribute1 in enumerate(bombs):
                x1, y1, r1 = attribute1
                
                if euclidean_distance(x, y, x1, y1) <= r:
                    graph[node].append(node1)
        def dfs(node):
            
            visited = set()
            stack = [node]
            visited.add(node)
            i = 0
            while stack:
                
                current = stack.pop()
            
                for neighbour in graph[current]:
                    
                    if not neighbour in visited:
                        stack.append(neighbour)
                        visited.add(neighbour)
                
            return visited
                
                    
        # now starting from each node what is the maximum nodes that I can visite using dfs
        max_visited = 0
        for sr in graph.keys():
            visited = dfs(sr)
            max_visited = max(max_visited, len(visited))
        
        return max_visited
            
            
        
        