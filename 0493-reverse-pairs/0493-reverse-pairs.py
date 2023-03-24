class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # [1, 3, 2, 3, 1]
        # [1] [2]  [3]
        
        #[1, 2] [3] 
        self.ans = 0
        nums = [[val, idx] for idx, val in enumerate(nums)]
        def count(left, right):
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > 2*right[j][0]:
                    self.ans += len(left) - i
                    j += 1
                else:
                    i += 1
           
        
        def divide(nums , start ,end):
            if end - start <= 0:
                return [nums[start]]
            
            mid = start + (end - start) // 2
            left = divide(nums, start , mid)
            right = divide(nums , mid + 1 , end)
            
            return merge(left , right)
        
        def merge(left , right):
            i = 0
            j = 0
            res = []
            count(left, right)
            
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            
            if i < len(left):
                res.extend(left[i:])
            if j < len(right):
                res.extend(right[j:])
            
            
            return res     
        
        divide(nums , 0 , len(nums) - 1)
        
        return self.ans
                
            
        