#User function Template for python3
from collections import defaultdict 
class Solution:
    def ToGraph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            
            u, v = edge
            graph[u].append(v)
        
        return graph
    def possible_paths(self, edges, n, s, d):
        graph = self.ToGraph(edges)
        stack = [s]
        count = 0
        while stack:
            current = stack.pop()
            if current == d:
                count += 1
            
            for neighbour in graph[current]:
                stack.append(neighbour)
        
        return count 
        
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, s, d = input().split()
		n = int(n); m = int(m); s = int(s); d = int(d);
		edges = []
		for _ in range(m):
		    x,y = input().split()
		    x = int(x); y = int(y);
		    edges.append([x,y])
		obj = Solution()
		ans = obj.possible_paths(edges, n, s, d)
		print(ans)


# } Driver Code Ends