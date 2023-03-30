class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(ans, visited, temp):
            
            if len(temp) == len(nums):
                ans.append(temp[:])
                return 
            
            for i in range(len(nums)):
                if visited & (1 << i) == 0:
                    temp.append(nums[i])
                    visited |= 1 << i
                    backtracking(ans, visited , temp)
                    temp.pop()
                    visited &= ~(1 << i)
        ans = []
        visited = 0
        temp = []
        
        backtracking(ans , visited,  temp)
        
        return ans
            
            
        