class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # intention
        # execution
        
        #etion 
        
        @cache
        def dp(i, j):
            
            if i == len(word1):
                
                return len(word2) - j
            
            if j == len(word2):
                
                return len(word1) - i
            
            ans = 0
            
            if word1[i] == word2[j]:
                
                return dp(i + 1, j + 1)
            
            else:
                
                ans = min(1 + dp(i + 1, j) , 1 + dp(i, j + 1) , 1 + dp(i + 1, j + 1))
            
            return ans
        
        return dp(0, 0)
                
            
                