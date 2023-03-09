class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
    
        bucket = [0] * k
        self.ans = sum(cookies)
        
        def backtrack(idx):
            
            if idx >= len(cookies):
                
                self.ans = min(self.ans , max(bucket))
                return
            
            if max(bucket) > self.ans:
                return
            
            for i in range(k):
                
                bucket[i] += cookies[idx]
                backtrack(idx + 1)
                bucket[i] -= cookies[idx]
                if bucket[i] == 0:
                    return 
                
        backtrack(0)
        
        return self.ans
        