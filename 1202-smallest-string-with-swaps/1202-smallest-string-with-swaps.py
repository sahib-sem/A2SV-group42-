# UnionFind class
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for a, b in pairs:
            uf.union(a, b)
        
        group = defaultdict(list)
        index = defaultdict(int)
        for idx in range(len(s)):
            
            rep = uf.find(idx)
            group[rep].append(s[idx])
        
        group = dict(group)
        group = {key:sorted(val) for key, val in group.items()}
        
        ans = ''
        for idx in range(len(s)):
            rep = uf.find(idx)
            i = index[rep]
            ans += group[rep][i]
            index[rep] += 1
        
        return ans 
        
        
        
            
        
        