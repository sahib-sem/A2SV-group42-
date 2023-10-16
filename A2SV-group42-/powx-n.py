class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def Pow(x, n):
            
            if n <= 0:
                return 1

            if n % 2 == 0:

                return Pow(x * x , n // 2)

            else:

                return x * Pow(x , n - 1)
            
        
        if n < 0:
            return Pow(1 / x , -n)
        
        return Pow(x, n)