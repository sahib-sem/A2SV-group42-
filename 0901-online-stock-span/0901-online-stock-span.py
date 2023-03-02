class StockSpanner:

    def __init__(self):
        self.stock = []
        self.stack = []
        self.index = 0

    def next(self, price: int) -> int:
        
        self.stock.append(price)
        count = 0
        index = self.index
        
        while self.stack and self.stack[-1][0] <= price:
            index = self.stack.pop()[1]
            count = self.index - index
        
        
        self.stack.append([price, index])
        self.index += 1
        
        return count + 1
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)