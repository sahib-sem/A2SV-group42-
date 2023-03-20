class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = set()
        
        def backtracking(temp, i):
            
            if len(temp) > 1:
                self.ans.add(tuple(temp))
            
            if i >= len(nums):
                return
            
            backtracking(temp , i + 1)
            
            if not temp or temp[-1] <=nums[i]:
                temp.append(nums[i])
                backtracking(temp , i + 1)
                temp.pop()
                
            
           
        backtracking([] , 0)
        return self.ans
            
            
            
            
            
            