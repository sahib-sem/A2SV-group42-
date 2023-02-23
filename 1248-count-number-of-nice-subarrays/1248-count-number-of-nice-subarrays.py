class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k,nums):
            ans = start = 0
            for end in range(len(nums)):
                k -= nums[end] % 2
                while k < 0:
                    k += nums[start] % 2
                    start += 1
                ans += end - start + 1
            return ans
        return atMost(k,nums) - atMost(k - 1,nums)
                
                    