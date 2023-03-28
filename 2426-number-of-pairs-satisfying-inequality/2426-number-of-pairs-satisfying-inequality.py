class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # [[3,0] , [2,1] , [5,2]]  [[2,0], [2 , 1] , [1, 1]]
       # brute force O(n ^ 2)
#         res = 0
        
#         for i in range(len(nums1)):
#             for j in range(i + 1 ,len(nums2)):
#                 if nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff:
#                     res += 1
        
#         return res
        
        difference = []
        for i in range(len(nums1)):
            difference.append(nums1[i] - nums2[i])
        self.ans = 0
        def update_ans(left, right, diff):
            
            
            for target in left:
                low = -1
                high = len(right)
                while high > low + 1:
                    mid = low + (high - low) // 2
                    
                    if right[mid] + diff < target:
                        low = mid
                    else:
                        high = mid
                        
                if high != len(right):
                    self.ans += len(right) - high
                
        
        def divide(nums , start , end,diff):
            if end - start <= 0:
                return [nums[start]]
            
            mid = start + (end - start) // 2
            left = divide(nums, start , mid, diff)
            right = divide(nums, mid + 1, end, diff)
            
            return merge(left, right, diff)
        
        def merge(left, right, diff):
            update_ans(left, right, diff)
            i = 0
            j = 0
            res = []
            
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
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
        
        divide(difference, 0 , len(difference) - 1, diff)
        
        return self.ans
                    
        
        
        
        
        
        