class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def recursive(n, k):
            if n == 1:
                return 0
            else:
                if k % 2 == 0:
                    return 1 - recursive(n - 1 , (k + 1) // 2)
                else:
                    return recursive(n-1 , (k + 1) // 2)
                
        return recursive(n, k)
        
        
        
        
        
        
        
        
        