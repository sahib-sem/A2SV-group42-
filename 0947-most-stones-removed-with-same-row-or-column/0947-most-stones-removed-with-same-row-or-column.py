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
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))
        rows = []
        cols = []
        
        for idx, (x, y) in enumerate(stones):
            rows.append((x, idx))
            cols.append((y, idx))
        rows.sort()
        cols.sort()
        
        i = 0
        while i < len(rows) - 1:
            r, node = rows[i]
            r1, node1 = rows[i + 1]
            if r == r1:
                uf.union(node, node1)
            i += 1
        j = 0
        while j < len(cols)  - 1:
            c, node = cols[j]
            c1, node1 = cols[j + 1]
            if c == c1:
                uf.union(node, node1)
            
            j += 1
        rep = [uf.find(val) for val in range(len(stones))]
        rep = Counter(rep)
        rep = [val - 1 for val in rep.values()]
        
       
            
        return sum(rep)
        
        
                
            
        
        
        