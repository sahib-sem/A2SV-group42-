class Solution:
    def numDecodings(self, s: str) -> int:
        #   226
        # let make a backtracking function 
        
        memo = {}
        
        
        def dp(i):
            
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            
            
            if i not in memo:
                
                
                ans1, ans2 = dp(i + 1) , dp(i + 2)
                
                if s[i] == '0':
                    ans1 = 0
                    ans2 = 0
                    
                if i < len(s) - 1 and s[i+ 1] == '0':
                    ans1 = 0
                
                if i < len(s) - 1 and int(s[i] + s[i + 1]) > 26:
                    ans2 = 0
                
                memo[i] = ans1 + ans2
                    
            
            return memo[i]
        
        return dp(0)
    
        