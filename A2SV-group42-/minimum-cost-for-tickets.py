class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        # [1, 4, 6, 7, 8, 20]
        
        pass_days = [1, 7, 30]
        
        @cache
        def dp(i):
            
            if i == len(days):
                return 0
            
            ans = float('inf')
            
            for idx, choice in enumerate(pass_days):
                pass_allowed = days[i] + choice
                j = i
                
                while j < len(days):
                    if days[j] >= pass_allowed:
                        break
                    j += 1
                
                ans = min(costs[idx] + dp(j), ans)
            
            
            return ans
        
        return dp(0)
                
                    
            
            