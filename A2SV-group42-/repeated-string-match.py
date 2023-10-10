class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        
        lps = [0] * len(b)
        
        i, j = 0, 1
        
        while j < len(b):
            
            if b[i] == b[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            
            elif i == 0:
                j += 1
                
            else:
                
                i = lps[i - 1]
        
        
        i, j = 0, 0
        ans = 1
        
        k = 0
        upper_limit = len(b) + 2 * len(a)
        
        while k < upper_limit:
            
            if a[i] == b[j]:
                
                i += 1
                j += 1
            
            elif j == 0:
                i += 1
            
            else:
                
                j = lps[j - 1]
            
            if j == len(b):
                return ans
            
            if i == len(a):
                i = 0
                ans += 1
            
            k += 1
            
            
        
        return -1
            
            
            
            
                
                
            
                
                
        
        