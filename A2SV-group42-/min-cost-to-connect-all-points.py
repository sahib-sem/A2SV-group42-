class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        all_manhatten_distance = []
        N = len(points)
        
        for i in range(N - 1):
            xi, yi = points[i]
            
            for j in range(i + 1, N):
                xj , yj = points[j]
                md = abs(xj - xi) + abs(yj - yi)
                all_manhatten_distance.append((md , i, j))
        
        all_manhatten_distance.sort()
        cost = 0
        
        uf = UnionFind(N)
        
        for c , i, j in all_manhatten_distance:
            if not uf.connected(i, j):
                cost += c
                uf.union(i, j)
        
        return cost
        
                
                
                
        