

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        root = { chr(i):chr(i) for i in range(97, 124)}
        def find(root, x):
            while x != root[x]:
                x = root[x]
            return x
        
        def union(x, y, root):
            x = find(root, x)
            y = find(root, y)
            if x < y:
                root[y] = x
            else:
                root[x] = y
        
        for i in range(len(s1)):
            chr1, chr2 = s1[i] , s2[i]
            union(chr1, chr2, root)
        
        ans = ''
        for char in baseStr:
            ans += find(root, char)
        
        return ans
        
        
        