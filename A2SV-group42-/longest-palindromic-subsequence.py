class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def LCS(text1, text2):
            n = max(len(text1) , len(text2)) + 1

            dp = [[0 for _ in range(n)] for __ in range(n)]

            for i in range(len(text1) - 1 , -1, -1):
                for j in range(len(text2) - 1 , -1, -1):

                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] += max(dp[i + 1][j] , dp[i][j + 1])

            return dp[0][0]
        
        return LCS(s , s[::-1])
        
        
            
            
            
             
            
                
            
            
            
            
        
        
        