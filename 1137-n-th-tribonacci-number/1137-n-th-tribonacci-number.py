class Solution:
    def tribonacci(self, n: int) -> int:
        
#         memo = {}
        
#         def trib(n):
#             if n <= 1:
#                 return n
#             if n == 2:
#                 return 1
            
#             if n not in memo:
#                 memo[n] = trib(n-1) + trib(n-2) + trib(n-3)
            
#             return memo[n]
        
#         return trib(n)
    
        # bottom up apprach 
        if n <= 1:
            return n
        if n == 2:
            return 1
        arr = [0] * (n + 1)
        arr[1] = arr[2] = 1
        
        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        
        return arr[n]

        
        