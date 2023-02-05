class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        operation=0
        while j>i:
            if nums[i]+nums[j]==k:
                print(i,j)
                i+=1
                j-=1
                operation+=1
            elif nums[i]+nums[j]>k:
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
        return operation
        
        