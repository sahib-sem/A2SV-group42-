class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = float('inf')
        profit = 0
        
        for i in range(len(prices)):
            
            sell = prices[i] - buy
            profit = max(sell, profit)
            buy = min(buy, prices[i])
        
        return profit 
            
        
        
        
        