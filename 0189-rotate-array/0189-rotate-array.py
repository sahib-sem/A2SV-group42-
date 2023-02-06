class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def shiftArray(lst):
            lst.insert(0,0)
            lst.pop()
                
               
        for i in range(k):
            temp=nums[-1]
            shiftArray(nums)
            nums[0]=temp
        return nums
            