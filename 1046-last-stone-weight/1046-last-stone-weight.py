class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * element for element in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            heapq.heappush(stones, x - y)
        
        return -1 * (heapq.heappop(stones))
        