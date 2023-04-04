class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        count = Counter(deck)

        values = list(count.values())
        gcd_val = values[0]
        for num in values:
            gcd_val = gcd(gcd_val , num)
        
        if gcd_val > 1:
            return True
        
            

        
        