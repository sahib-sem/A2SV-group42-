# UnionFind class
class UnionFind:
    def __init__(self):
        self.root = {chr(i):chr(i) for i in range(97, 124)}
        self.rank = {chr(i):1 for i in range(97, 124)}

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
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind()
        equal = []
        not_equal = []

        for equation in equations:
            var1, eq, var2 = equation[0] , equation[1:3] , equation[-1]
            if eq == '==':
                equal.append(equation)
                
            else:
                not_equal.append(equation)
        for equation in equal:
            var1, eq, var2 = equation[0] , equation[1:3] , equation[-1]
            uf.union(var1, var2)
        
        for equation in not_equal:
            var1, eq, var2 = equation[0] , equation[1:3] , equation[-1]
            if uf.connected(var1, var2):
                return False
            
            
            
        return True
            
            
        
        