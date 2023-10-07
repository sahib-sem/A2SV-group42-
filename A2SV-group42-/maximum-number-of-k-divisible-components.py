class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        
        tree = defaultdict(list)
        
        for a, b in edges:
            
            tree[a].append(b)
            tree[b].append(a)
            
        ans = 0
        
        def dfs(curr, visited = set({})):
            
            nonlocal ans
        
            curr_sum = values[curr]
            visited.add(curr)
            
            for child in tree[curr]:
                
                if child not in visited:
                    curr_sum += dfs(child, visited)
            
            if curr_sum % k == 0:
                
                ans += 1
                return 0
            
            return curr_sum
        
        dfs(0)
        
        return ans
    