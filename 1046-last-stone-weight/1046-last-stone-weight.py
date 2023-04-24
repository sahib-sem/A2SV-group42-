class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            insort(stones, y - x)
        
        return stones[0]
        