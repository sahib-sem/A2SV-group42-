class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        cost.append(0)
        
        def dp(i, ans):
            if i == -1:
                return 0
            if i == 0:
                return cost[0]
            
            if i not in memo:
                
                memo[i] = cost[i]  + min(dp(i - 2, ans), dp(i - 1, ans))
            ans += memo[i]
            
            return ans
        
        return dp(len(cost) - 1, 0)
        
        