class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.group_max_dis = [-1] * size
        
        
    def find(self, x):
       
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
        

    # The union function with union by rank
    def union(self, x, y):
        
        rootX  = self.find(x)
        rootY  = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
    
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        
        

    def connected(self, x, y):
        return self.find(x) == self.find(y)
           
    

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        ii = 0
        uf = UnionFind(n)
        ans = [False] * (len(queries))
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        
        edgeList = sorted((w, u, v) for  u, v, w in edgeList)
        
        
        for w, p, q, i in queries:
            while ii < len(edgeList) and edgeList[ii][0] < w:
                _, u, v = edgeList[ii]
                uf.union(u, v)
                ii += 1
            
            ans[i] = uf.connected(p, q)
        
        return ans
            
            
                
        
                 
            
            
        
        
                
        
        
        