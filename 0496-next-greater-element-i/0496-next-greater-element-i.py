class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        res = []
        
        stack.append(nums2[0])
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()
                
            stack.append(nums2[i])
        
        for num in stack:
            next_greater[num] = -1
        
        for num in nums1:
            res.append(next_greater[num])
        return  res
        
            
        
        