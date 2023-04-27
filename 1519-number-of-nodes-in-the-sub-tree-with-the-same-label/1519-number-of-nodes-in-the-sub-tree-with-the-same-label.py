class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = {i:[] for i in range(len(labels))}
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        def toInt(char):
            return ord(char) - 97
        def addLst(lst1, lst2):
            for i in range(len(lst1)):
                lst1[i] += lst2[i]
                
            return lst1
        self.ans = [0 for _ in range(len(labels))]
        def dfs(root, visited):
            if len(graph[root]) == 1 and root != 0:
                lst = [0 for _ in range(26)]
                idx = toInt(labels[root])
                lst[idx] = 1
                self.ans[root] = 1
                return lst
            
            visited.add(root)
            res = [0 for _ in range(26)]
            idx1 = toInt(labels[root])
            res[idx1] = 1
            for neighbour in graph[root]:
                if neighbour not in visited:
                    lst = dfs(neighbour , visited)
                    res = addLst(res, lst)
            
            self.ans[root] = res[toInt(labels[root])]
        
            return res
        
        dfs(0, set())
        
        return self.ans
                
                    
                    
                    
            
            
            
            
            