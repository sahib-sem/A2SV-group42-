class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        stack = []
        next_greater = [-1] * n
        
        for i in range(2*n):
            
            i = i % n
            while stack and stack[-1][0] < nums[i]:
                removed = stack.pop()
                next_greater[removed[1]] = nums[i]
            
            stack.append([nums[i] , i])
            
        print(next_greater )
        return next_greater
                
        