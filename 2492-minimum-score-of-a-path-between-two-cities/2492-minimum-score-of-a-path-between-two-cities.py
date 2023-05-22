# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        to_be_sorted = []
        uf = UnionFind(n + 1)
        
        for a, b, cost in roads:
            uf.union(a, b)
            to_be_sorted.append((cost, a))
        
        to_be_sorted.sort()
        for cost, node in to_be_sorted:
            if uf.connected(node, n):
                return cost
        
        
        
                
                
        