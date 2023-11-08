class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l , h = 0 , len(nums) - 1

        while l <= h:

            mid = l + (h - l) // 2
            print(l, h, mid)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[h] >= target >= nums[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
        
        return -1

        



        
        