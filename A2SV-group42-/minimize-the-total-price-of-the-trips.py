class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        

        graph = defaultdict(list)
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)
    
        # function to find the minimum path cost between two nodes
        def search(current, target, most_refered_node , parent = None):
             
            
            if current == target:
                most_refered_node[current] += 1
                return True
            
            ans = False
            
            for nei in graph[current]:
                if nei != parent:
                    result =  search(nei, target, most_refered_node, current)
                    ans = result or ans
                    
            if ans:
                most_refered_node[current] += 1
            
            return ans
                    
                        
                    
                    
            
        
        total = 0
        frequency = defaultdict(int)
        
        for start, target in trips:
            search(start, target, frequency)
        
        def dp(v,visited = set({})):
            
            
            
            visited.add(v)
            ans = [frequency[v] * price[v] ,frequency[v] * (price[v] // 2)  ]        
            total1, total2 = 0, 0
            for nei in graph[v]:
                
                if nei not in visited:
                    nonhalved, halved = dp(nei, visited)
                    ans[0] += min(nonhalved, halved)
                    ans[1] += nonhalved
   
            return ans
            
        memo = {}           
        sub = min(dp(0))
        
        return sub
                    
                    
                    
                    
                    
                    
                    
            
        
            
            
            
            
        