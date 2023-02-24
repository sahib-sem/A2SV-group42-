class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.head = 0
        self.end = 0
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        
        if not self.isFull():
            self.queue[self.end] = value
            self.end += 1
            self.end %= self.k
            self.size += 1
            return True
        
        

    def deQueue(self) -> bool:
        
        if not self.isEmpty():
            
            self.queue[self.head] = -1 
            self.head += 1
            self.head %= self.k
            self.size -= 1
            return True
        return False
            
            

    def Front(self) -> int:
        return self.queue[self.head]
        

    def Rear(self) -> int:
        return self.queue[self.end - 1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()