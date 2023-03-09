class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # base case len(candidate) == k
        # list_candidate = []
        
        
        def backtrack(comb , lst ,ans, i, k):
            if len(comb) == k:
                ans.append(comb[:])
                return 
                
            if i >= len(lst):
                return
            
            backtrack(comb , lst ,ans, i+1,k)
            comb.append(lst[i])
            backtrack(comb ,lst ,ans,i + 1,k)
            comb.pop()
        
        comb = []
        i = 0
        lst = [i for i in range(1, n + 1)]
        ans = []
        backtrack(comb , lst ,ans, i , k)
        
        return ans
            
            
                
            
        