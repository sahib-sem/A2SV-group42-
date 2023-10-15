class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        # at even index have 5 choices 0, 2, 4, 6, 8
        # at odd index have 4 choices 2, 3, 5, 7
        
        # 5 ** ceil(n/ 2) + 4 ** floor(n / 2)
        
        mod = 1000000007
        
        ans = 1
        
        even = ceil(n / 2)
        odd = floor(n / 2)
        
        return (pow(5, even, mod) * pow(4, odd, mod)) % mod
        
        