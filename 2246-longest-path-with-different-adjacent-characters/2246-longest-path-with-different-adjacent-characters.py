class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        '''
        
        '''
        
        graph = {i:[] for i in range(len(parent))}
        for i, val in enumerate(parent):
            if val == -1:
                root = i
                continue
            graph[val].append(i)
        
        self.ans = 0
        def dfs(node):
            
            res_lst = []
            for neighbour in graph[node]:
                res = dfs(neighbour)
                if s[node] == s[neighbour]:
                    res = 0
                res_lst.append(res)
            
            res_lst.sort(reverse = True)
            
            if len(res_lst) >= 2:
                self.ans = max(self.ans , 1 + res_lst[0] + res_lst[1])
                return 1 + max(res_lst[0] , res_lst[1])
                
            elif len(res_lst) == 1:
                self.ans = max(self.ans , 1 + res_lst[0])
                return 1 + res_lst[0]
            else:
                self.ans = max(self.ans , 1)
                return 1
        dfs(root)
        
        return self.ans 
            
                
                    
                