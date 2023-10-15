class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        
        '''
        
        1: {2} , 
        
        '''
        
        rather = {}
        
        for a, b in pairs:
            
            a_rather = []
            b_rather = []
            
            for a_p in preferences[a]:
                
                if a_p == b:
                    break
                a_rather.append(a_p)
            
            for b_p in preferences[b]:
                
                if b_p == a:
                    break
                b_rather.append(b_p)
            
            
            rather[a] = set(a_rather)
            rather[b] = set(b_rather)
        
        ans = 0
        
        
        
        for a, b in pairs:
            
            a_have , b_have = False, False
            for a_p in rather[a]:
                
                if a in rather[a_p]:
                    a_have = True
                
                if a_have: break
            for b_p in rather[b]:
                
                if b in rather[b_p]:
                    b_have = True
                
                if b_have: break
            
            ans += int(a_have) + int(b_have)
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        