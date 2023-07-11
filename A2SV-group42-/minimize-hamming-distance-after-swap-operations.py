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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # source = [1, 2, 3, 4] [[0, 1] , [2, 3]]
        # target = [2, 1, 4, 5]
        
        n = len(source)
        uf = UnionFind(n)
        
        sr_dict = defaultdict(list)
        tar_dict = defaultdict(list)
        
        swaps = set()
        
        def hamming_distance(lst1 , lst2):
            lst_c1 = dict(Counter(lst1))
            lst_c2 = dict(Counter(lst2))
            similar = 0
            
            for key in lst_c1:
                similar += min(lst_c1.get(key, 0) , lst_c2.get(key, 0))
            
            return len(lst1) - similar
                
        
        for i, j in allowedSwaps:
            uf.union(i, j)
            swaps.add(i)
            swaps.add(j)
        
        for i in swaps:
            
            sr_dict[uf.find(i)].append(source[i])
            tar_dict[uf.find(i)].append(target[i])
        
        ans = 0
        diff = set(range(n)).difference(swaps)
        for j in diff:
            if source[j] != target[j]:
                ans += 1
        
        for val1, val2 in zip(sr_dict.values() , tar_dict.values()):
            ans += hamming_distance(val1, val2)
           

        return ans
        
        
        
        
        