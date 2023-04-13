class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # dfs coloring 
       # 1 - group1 and -1 - group2
        
        graph = defaultdict(list)
        arr = [0 for _ in range(n)]
        
        for a, b in dislikes:
            graph[a].append(b)
        
        for key in graph.keys():
            if arr[key - 1]:
                continue
            stack = [key]
            arr[key - 1] = 1
            while stack:

                current = stack.pop()
                
                if current in graph:
                    for neighbour in graph[current]:
                        if arr[neighbour - 1] == 0:
                            stack.append(neighbour)
                            arr[neighbour - 1] = -1 * arr[current - 1]
                        elif arr[neighbour - 1] ==  arr[current - 1]:
                            
                            return False
            arr = [0 for _ in range(n)]
       
        return True
                    
                    