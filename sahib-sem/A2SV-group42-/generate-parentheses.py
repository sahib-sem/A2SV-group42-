class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtrack(left_bracket, right_bracket , temp = [], idx = 0):
            if idx >= 2 * n:
                ans.append(''.join(temp[:]))
                return 
            
            if left_bracket > 0:
                temp.append('(')
                backtrack(left_bracket - 1 , right_bracket, temp , idx + 1)
                temp.pop()
            if left_bracket < right_bracket and right_bracket > 0:
                temp.append(')')
                backtrack(left_bracket , right_bracket - 1 , temp , idx + 1)
            
                temp.pop()
        
        backtrack(n , n)
        
        return ans
            
            
            