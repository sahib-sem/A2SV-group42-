class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)
        img1_ones = set({})
        img2_ones = set({})
        
        for r in range(n):
            for c in range(n):
                
                if img1[r][c] == 1:
                    img1_ones.add((r, c))
                if img2[r][c] == 1:
                    img2_ones.add((r, c))
        
        
        def apply_transformation(l, r):
            
            transformed = set({})
            
            for x, y in img2_ones:
                
                transformed.add((x + l, y + r))
            
            return len(img1_ones.intersection(transformed))
        
        ans = 0
        
        for l in range(-n , n):
            
            for r in range(-n, n):
                
                ans = max(ans, apply_transformation(r, l))
        
        return ans
        