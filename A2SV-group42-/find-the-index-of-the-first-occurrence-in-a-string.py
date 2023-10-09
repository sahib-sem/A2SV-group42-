class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        m = len(needle)
        n = len(haystack)
        
        lps = [0] * m
        
        if len(needle) > len(haystack):
            return -1
        
        i, j = 0, 1
        
        while j < m:
            
            if needle[i] == needle[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            
            elif i == 0:
                j += 1
            
            else:
                i = lps[i - 1]
        
        n_i, h_i = 0, 0
        
        
        while h_i < n:
            
            if haystack[h_i] == needle[n_i]:
                
                h_i += 1
                n_i += 1
            
            elif n_i == 0:
                h_i += 1
            else:
                
                n_i = lps[n_i - 1]
            
            if n_i == m:
                
                return h_i - m
        
        return -1
            
            
        
    
        