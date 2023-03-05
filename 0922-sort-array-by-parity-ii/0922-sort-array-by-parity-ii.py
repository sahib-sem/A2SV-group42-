class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        l = 0
        while l < len(nums):
            if l % 2 == 0:
                if nums[l] % 2 == 0:
                    l += 1
                else:
                    r = l + 1
                    # find the first even num and swap
                    while r < len(nums):
                        if nums[r] % 2 == 0:
                            nums[l] , nums[r] = nums[r] , nums[l]
                            break
                        r += 1
                    
            else:
                if nums[l] % 2 != 0:
                    l += 1
                else:
                    r = l + 1
                    
                    while r < len(nums):
                        if nums[r] % 2 != 0:
                            nums[l] , nums[r] = nums[r] , nums[l]
                            break
                        r += 1
        return nums