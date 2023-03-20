class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        self.res = 0
        self.ans = []
        def backtrack( comb , i, k):
            if len(comb) == k:
                self.ans.append(comb[:])
                return 

            if i >= len(requests):
                return

            backtrack( comb ,i + 1 ,k )
            comb.append(requests[i])
            backtrack( comb ,i + 1, k)
            comb.pop()
                    
        def checkValid(comb):
            count = defaultdict(int)
            for fr , end in comb:
                count[fr] -= 1
                count[end] += 1
            
            valid = True
            for i in count.values():
                if i != 0:
                    valid = False
                    break
            
            if valid:
                self.res = max(self.res , len(comb))
                
        for i in range(len(requests) + 1):
            self.ans = []
            backtrack( [] , 0 , i)
            for j in self.ans:
                checkValid(j)
        
        return self.res
            
            
            
            
            
                
        
        