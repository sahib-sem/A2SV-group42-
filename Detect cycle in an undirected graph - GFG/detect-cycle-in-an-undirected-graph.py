from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    inDegree = [0 for _ in range(V)]
	    
	    for edge in adj:
	        for e in edge:
	            inDegree[e] += 1
	    queue = deque([])
	    visited= set()
	   
	    for i in range(V):
	        if inDegree[i] <= 1:
	            queue.append(i)
	            visited.add(i)
	    order = []
	   
	    while queue:
	       
	        current = queue.popleft()
	        order.append(current)
	        visited.add(current)
	        for nei in adj[current]:
	            if nei not in visited:
    	            inDegree[nei] -= 1
    	           
    	            if inDegree[nei] == 1:
    	                queue.append(nei)
    	                
    	            
        
        
        if len(order) < V:
            return 1
           
        return 0
	       
	           
	    
	    
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends