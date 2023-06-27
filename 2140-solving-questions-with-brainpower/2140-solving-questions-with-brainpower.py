class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # similar question with house robber
        
        memo = {}
        
        def dp(i):
            
            if i == len(questions) - 1:
                return questions[len(questions) - 1][0]
            
            if i > len(questions) - 1:
                return 0
            
            if i not in memo:
                memo[i] = max(questions[i][0] + dp(i + questions[i][1] + 1) , dp(i + 1))
            
            return memo[i]
        
        return dp(0)
        
        
        
            
            