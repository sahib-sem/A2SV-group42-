class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap , num)
        else:
            heapq.heappush(self.max_heap, -1 * num)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap , -1 * heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            x = self.min_heap[0]
            y = self.max_heap[0]
            return (x + -1 * y) / 2
        else:
      
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()