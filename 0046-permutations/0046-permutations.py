class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(ans, visited, temp):
            
            if len(temp) == len(nums):
                ans.append(temp[:])
                return 
            
            for i in nums:
                if not i in visited:
                    temp.append(i)
                    visited.add(i)
                    backtracking(ans, visited , temp)
                    temp.pop()
                    visited.remove(i)
        ans = []
        visited = set()
        temp = []
        
        backtracking(ans , visited,  temp)
        
        return ans
            
            
        