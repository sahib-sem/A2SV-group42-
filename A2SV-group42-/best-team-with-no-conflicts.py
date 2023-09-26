class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        lst = []
        n = len(scores)
        
        for i in range(n):
            lst.append((ages[i], scores[i]))
        
        lst.sort()
        
        dp = [0] * len(lst)
        
        for i in range(len(lst)):
            
            dp[i] = lst[i][1]
        
        i = 0
        
        
        while i < len(lst):
            
            j = 0
            
            max_val = 0
            
            while j < i:
                
                if lst[i][1] >= lst[j][1] or lst[i][0] == lst[j][0]:
                    
                    max_val = max(dp[j], max_val)
                
                j += 1
            
            
            dp[i] += max_val
        
            i += 1
        
        
        return max(dp)
                    
                    
                
            
            
        
        
                    
                    
                    
                    
            
            
            
            
            
            
        
        
        
        
        
                
                
                
                    
                    
        
        
        
        
        
        
        
        
        
        