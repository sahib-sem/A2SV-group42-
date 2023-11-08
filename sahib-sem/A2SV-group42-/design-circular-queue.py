class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.capacity > 0:
            
            self.queue[self.rear] = value
            self.rear += 1
            self.rear %= len(self.queue)
            self.capacity -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.capacity < len(self.queue):
            self.front += 1
            self.front %= len(self.queue)
            self.capacity += 1
            return True

        return False

    def Front(self) -> int:
        if self.capacity < len(self.queue):
            return self.queue[self.front]
        return  - 1
        

    def Rear(self) -> int:
        if self.capacity < len(self.queue):
            return self.queue[self.rear - 1]
        return - 1
        

    def isEmpty(self) -> bool:
        return self.capacity == len(self.queue)

    def isFull(self) -> bool:
        return self.capacity == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()