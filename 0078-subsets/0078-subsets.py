class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(comb , lst ,ans, i, k):
            if len(comb) == k:
                ans.append(comb[:])
                return 

            if i >= len(lst):
                return

            backtrack(comb ,lst, ans, i+1 ,k )
            comb.append(lst[i])
            backtrack(comb ,lst, ans, i+1 ,k)
            comb.pop()
        lst = nums
        ans = []
        for i in range(len(nums) + 1):
            comb = []
            j = 0
            k = i
            backtrack(comb , lst ,ans, j , k)
        
        return ans    
        