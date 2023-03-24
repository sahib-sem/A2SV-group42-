class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        temp = []
        while i < len(nums):
            if nums[i] != i + 1:
                swap = nums[i] - 1
                if nums[swap] != swap + 1:
                    nums[i] , nums[swap] = nums[swap] , nums[i]
                else:
                    
                    temp.append(i)
                    i += 1
            else:
                i += 1
        ans = []
        for t in temp:
            if nums[t] != t + 1:
                ans.append(t + 1)
        return ans