class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            new_string = ''
            for char in s:
                if char == '0':
                    new_string += '1'
                else:
                    new_string += '0'
            return new_string
        
        def S(n):
            if n == 1:
                return '0'
            return S(n - 1) + '1' + invert(S(n - 1))[::-1]
        
        return S(n)[k - 1]
        
        