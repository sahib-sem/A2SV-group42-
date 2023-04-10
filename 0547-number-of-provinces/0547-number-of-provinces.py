class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        # {1: [2] , 2: [1] , 3: []}
        graph = defaultdict(list)
        m , n = len(isConnected) , len(isConnected[0])
        for r in range(m):
            for c in range(n):
                if isConnected[r][c] == 1:
                    graph[r + 1].append(c + 1)
        print(graph)
        def explore(graph , key , visited):
            stack = [key]
            while stack:
                current = stack.pop()
                visited.add(current)
                for neighbour in graph[current]:
                    if neighbour not in visited:
                        stack.append(neighbour)
            
            return visited
        
        visited = set()
        count = 0
        for key in graph.keys():
            if key not in visited:
                count += 1
                visited = explore(graph , key , visited)
        
        return count 
                
                
        
        
        
        
    
        