class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        lst = []
        cost = 0
        for num in instructions:
            left = bisect_left(lst, num)
            right = len(lst) - bisect_right(lst , num)
            cost += min(left, right)
            
            insort(lst, num)
        
        return cost % (10 ** 9 + 7)
            
            
        