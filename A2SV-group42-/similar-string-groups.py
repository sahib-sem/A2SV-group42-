class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        
        '''
        
        axaxax
        xaaxax
        
        
        '''
        
        union_find = {}
        
        for string in strs:
            union_find[string] = string
        
        
        def find(x):
            
            if x == union_find[x]:
                return x
            
            union_find[x] = find(union_find[x])
            return union_find[x]
        
        def union(x, y):
            
            repX = find(x)
            repY = find(y)
            
            if repX != repY:
                
                union_find[repX] = repY
        
        def check_similar(str1, str2):
            
            n = len(str1)
            
            diff = 0
            for i in range(n):
                
                if str1[i] != str2[i]:
                    
                    diff += 1
            
            return diff <= 2
        
        for i in range(len(strs)):
            
            str1 = strs[i]
            
            for j in range(i + 1, len(strs)):
                str2 = strs[j]
                
                if check_similar(str1, str2):
                    union(str1, str2)
        
        
        ans = set({})
        for string in union_find:
            ans.add(find(string))
        
        
        return len(ans)
            
        
                
                
            
            
        
        
        
        
                    
            
            
            
        