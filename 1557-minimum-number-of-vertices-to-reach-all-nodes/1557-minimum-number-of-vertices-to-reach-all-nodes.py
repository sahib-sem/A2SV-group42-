class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # first change to adjacency list 
        
            
            
        def changeToAdjList(edgeList):
            graph = {}
            for edge in edgeList:
                a, b = edge
                if not a in graph:
                    graph[a] = []
                if not b in graph:
                    graph[b] = []
                graph[a].append(b)
            return graph
        graph = changeToAdjList(edges)
        
        lst = set([i for i in range(n)])
        for node in graph:
            for n in graph[node]:
                lst.discard(n)
        return list(lst)
        