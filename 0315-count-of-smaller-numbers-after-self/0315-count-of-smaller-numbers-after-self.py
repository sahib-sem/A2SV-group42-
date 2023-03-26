class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # [[5,0] , [2,1], [6,1] , [1,3]]
        # [5,0] [2,1]
        #[2,5]   [1,6]
        #[2,1,1,0]
        
        self.ans = [0] * len(nums)
        nums = [[val, idx] for idx, val in enumerate(nums)]
        
        def update_ans(left, right):
            temp = [0] * len(left)
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    temp[i] += 1
                    j += 1
                else:
                    i += 1
            for idx in range(1, len(temp)):
                temp[idx] += temp[idx - 1]
            
            for ele , count in zip(left, temp):
                idx = ele[1]
                self.ans[idx] += count
            
            
                
        
        def divide(nums , start ,end):
            if end - start <= 0:
                return [nums[start]]
            
            mid = start + (end - start) // 2
            left = divide(nums, start , mid)
            right = divide(nums , mid + 1 , end)
            
            return combine(left , right)
        
        def combine(left , right):
            i = 0
            j = 0
            res = []
            update_ans(left, right)
            
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
        
        divide(nums, 0 , len(nums) - 1)
        
        return self.ans
            
        