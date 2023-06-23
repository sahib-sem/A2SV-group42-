class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def dp(rem_sum):
            
            if rem_sum < 0:
                return 0
            
            if rem_sum == 0:
                return 1
            
            total_ways = 0
            
            for num in nums:
                
                if rem_sum - num not in memo:
                    
                    memo[rem_sum - num] = dp(rem_sum - num)
                
                total_ways += memo[rem_sum - num]
            
            return total_ways 
        
        return dp(target)
            
            
        