class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        
        union_find = {chr(i):chr(i) for i in range(ord('a') , ord('a') + 26)}
        
        def union(x, y):
            repX = find(x)
            repY = find(y)
            if repX < repY:
                union_find[repY] = repX
            else:
                union_find[repX] = repY
        
        def find(x):
            
            if x == union_find[x]:
                return x
            
            union_find[x] = find(union_find[x])
            
            return union_find[x]
        
        
        
        for i in range(len(s1)):
            
            union(s1[i], s2[i])
        
        ans = []
        
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        
        return "".join(ans)
                    
                
            
            