class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ## [ 1, 2, 4]
        # [7, 6,4]
        
        def build_graph(edges, n):
            graph = {i : [] for i in range(n)}
            for x, y in edges:
                graph[x].append(y)
                graph[y].append(x)
            
            return graph
        
        def explore(node, graph, count):
            queue = deque()
            queue.append(node)
            res = 0
            visited.add(node)
            while queue:
                current = queue.pop()
                res += 1
                for neighbour in graph[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
            count.append(res)
            
        graph = build_graph(edges, n)
        visited = set()
        count = []
        for node in graph.keys():
            if node not in visited:
                explore(node, graph, count)
        prefix_sum = count[:]
        for i in range(len(count) - 2 , -1 , -1):
            prefix_sum[i] += prefix_sum[i + 1]
            
        prefix_sum.append(0)
        res = 0
        
        for idx, c in enumerate(count):
            res += c * prefix_sum[idx + 1]
    
        return res
        
        
        
        