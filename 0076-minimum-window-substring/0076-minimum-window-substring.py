class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        
        t_count = dict(Counter(t))
        s_count = {}
        
        have , need = 0 , len(t_count)
        start = 0
        res , resLen = [-1 , -1] , len(s) + 1
        
        for end in range(len(s)):
            
            s_count[s[end]] = s_count.get(s[end] , 0) + 1
            
            if s[end] in t_count and s_count[s[end]] == t_count[s[end]]:
                have += 1
                
            
            while have == need:
                # updating our results
                if (end - start + 1) < resLen:
                    
                    resLen = end - start + 1
                    res = [start , end]
                    
                # shrinking our window
                s_count[s[start]] -= 1
                if s[start] in t_count and s_count[s[start]] < t_count[s[start]]:
                    have -= 1
                start += 1
        return s[res[0]:res[1] + 1] if resLen < len(s) + 1 else ''
                
                
                    
                    
                
                
                
                    
                        
                    
                    
                        
                    
            
            
                
                
            
            
        
        
        
        