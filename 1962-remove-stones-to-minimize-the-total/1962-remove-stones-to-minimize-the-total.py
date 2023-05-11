class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1 * pile for pile in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            max_val = heapq.heappop(piles)
            heapq.heappush(piles, max_val - math.ceil(max_val / 2))
        
        return -1 *sum(piles)
        