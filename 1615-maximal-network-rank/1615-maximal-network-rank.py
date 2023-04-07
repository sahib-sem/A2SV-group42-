class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # first change to adjacency list 
        # pick two nodes with highest number of edges and
        # conditionaly substract one if there is an edge between them
        
        graph = defaultdict(list)
        
        def is_there_edge(a, b , graph):
                
            return a in graph[b]
        
        for road in roads:
            a, b = road
            graph[a].append(b)
            graph[b].append(a)
        
        lst = []
        
        for node , val in graph.items():
            lst.append([len(val) , node])
        
        max_val = 0
        for i in lst:
            for j in lst:
                if i == j:
                    continue
                val = i[0] + j[0]
                if is_there_edge(i[1] , j[1] , graph):
                    val -= 1
                max_val = max(val, max_val)
        
        return max_val 
                
        
        
        
            
        