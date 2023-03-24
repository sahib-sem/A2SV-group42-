class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.ans = nums[0]
        def quickselect(nums , start , end , k):
            if end - start <= 0:
                self.ans = nums[start]
                return 
            
            
            pivot = nums[start]
            write = start + 1
            for read in range(start + 1, end + 1):
                if nums[read] <= pivot:
                    nums[write] , nums[read] = nums[read] , nums[write]
                    write += 1
            nums[start] , nums[write - 1] = nums[write - 1] , nums[start]
            length = end - write + 2
            if  length == k:
                
                self.ans  = nums[write - 1] 
                return 
            if k < length:
                quickselect(nums, write , end , k)
            else:
                quickselect(nums, start , write - 2 , k - length)
        
        quickselect(nums, 0 , len(nums) - 1, k)
        return self.ans
            
            
            
        
        