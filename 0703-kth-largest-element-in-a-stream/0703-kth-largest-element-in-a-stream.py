class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)
        self.k = k
        
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        
        if self.heap[0] >= val:
            return self.heap[0]
        else:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]
            
        
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)