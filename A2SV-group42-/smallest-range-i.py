class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        maxx = max(nums)
        minn = min(nums)
        
        return max(0, maxx - minn - 2 * k)
                
                