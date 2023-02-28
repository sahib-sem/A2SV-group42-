class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        reverse_nums = sorted(nums,reverse = True)
        permutation = [0] * (n+ 1)
        
        for request in requests:
            
            l , r = request
            permutation[l] += 1
            permutation[r + 1] -= 1
            
        for i in range(1, n+1):
            
            permutation[i] += permutation[i - 1]
        
        permutation_mapping = [[i,n] for i , n in enumerate(permutation)]
        permutation_mapping = sorted(permutation_mapping , key = lambda x:x[1],reverse = True)
        
        ans = 0
        for i in range(n):
            
            if permutation_mapping[i][1] > 0:
                
                value = permutation_mapping[i][1]
                ans += value * reverse_nums[i]
                
            else:
                break
                
        return ans % mod
            
        
        
        
            
            
        