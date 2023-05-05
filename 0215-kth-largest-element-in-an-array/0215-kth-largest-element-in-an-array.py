class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * x for x in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -1 * heapq.heappop(nums)
            
            
            
        
        