class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0 
        ans = []
        while i < len(nums):
            if nums[i] != i + 1:
                swap = nums[i] - 1
                if nums[swap] != swap + 1:
                    nums[swap] , nums[i] = nums[i] , nums[swap]
                else:
                    if nums[i] not in ans:
                        ans.append(nums[i])
                    i += 1
            else:
                i += 1
        
        return ans
                    