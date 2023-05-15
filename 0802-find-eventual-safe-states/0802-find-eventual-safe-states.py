class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for _ in range(len(graph))]
        
        def dfs(node, colors, ans):
            
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            for nei in graph[node]:
                if colors[nei] == 2:
                    continue
                if not dfs(nei, colors, ans):
                    return False
            
            colors[node] = 2
            ans.append(node)
            return True
        
        ans = []
        for node in range(len(graph)):
            if colors[node]:
                continue
            dfs(node, colors, ans)
        
        return sorted(ans)
        
        
            
            
            
        