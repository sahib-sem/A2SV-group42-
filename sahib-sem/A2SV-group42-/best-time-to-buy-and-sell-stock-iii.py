class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(i, buy, num_transaction):
            
            if num_transaction == 2 or i == len(prices):
                return 0
            
            if buy:
                
                return max(dp(i + 1, buy , num_transaction), prices[i] + dp(i + 1, not buy, num_transaction + 1))
            
            else:
                
                return max(dp(i + 1, buy, num_transaction), -prices[i] + dp(i + 1, not buy, num_transaction))
        
        return dp(0, False, 0)