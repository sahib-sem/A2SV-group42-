class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        ans = 0
        sum_ = 0
        for num in nums:
            sum_ += num
            ans += count.get(sum_ - k,0)
            count[sum_] = count.get(sum_,0) + 1
        return ans 
            
            
            