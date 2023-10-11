class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        '''
        
        min(greater_than_me , less_than_me)
        
        min(less_than_me, greater_than_me)
        
        
        
        
        '''
        
        
        def less_than_greater_than(i):
            
            less_left = 0
            greater_left = 0
            less_right = 0
            greater_right = 0
            
            for j in range(i):
                
                if rating[i] > rating[j]:
                    less_left += 1
                
                elif rating[i] < rating[j]:
                    greater_left += 1
            
            for j in range(i + 1, len(rating)):
                
                if rating[i] > rating[j]:
                    less_right += 1
                
                elif rating[i] < rating[j]:
                    greater_right += 1
            
            return [less_left, greater_left, less_right, greater_right]
        
        ans = 0
        
        for i in range(1, len(rating)):
            
            l_left, g_left, l_right, g_right = less_than_greater_than(i)
            
            
            ans += l_left * g_right
            
            
            ans += g_left * l_right
        
        return ans
                    
                    
                    
        