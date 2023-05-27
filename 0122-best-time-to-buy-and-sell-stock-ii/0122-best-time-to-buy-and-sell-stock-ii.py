class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices):
            buy, sell = prices[i], prices[i]
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
                sell = prices[i]
            profit += sell - buy
            i += 1
        
        return profit
            
                
            
        