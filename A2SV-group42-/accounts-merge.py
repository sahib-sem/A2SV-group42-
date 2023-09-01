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
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        emails_identifier = {}
        idx = 0
        for account in accounts:
            
            name = account[0]
            
            for i in range(1, len(account)):
                
                if account[i] not in emails_identifier:
                    email = account[i]
                    
                    emails_identifier[email] = (idx, name)
                    idx += 1
        
        uf = UnionFind(len(emails_identifier))
        reverse = {}
        
        for account in accounts:
            
            if len(account) == 2:
                
                email = account[1]
                idx , name = emails_identifier[email]
                
                reverse[idx] = (email, name)
    
            
            for i in range(1, len(account) - 1):
                
                email1 = account[i]
                idx1, name1 = emails_identifier[email1]
                
                reverse[idx1] = (email1, name1)
                
                email2 = account[i + 1]
                idx2 , name2 = emails_identifier[email2]
                
                reverse[idx2] = (email2, name2)
                
                uf.union(idx1, idx2)
            
            
        
        ans = defaultdict(list)
        
        for i in range(len(emails_identifier)):
            
            email, name = reverse[i]
            
            rep = uf.find(i)
            
            
            ans[rep].append(email)
        
        res = []
        
        for key, val in ans.items():
            key = reverse[key][1]
            temp = [key]
            
            val.sort()
            temp.extend(val)
            
            res.append(temp)
        
        return res
                
                
        
        
        
        
        