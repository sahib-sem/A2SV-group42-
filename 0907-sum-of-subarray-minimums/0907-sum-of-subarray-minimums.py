class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        previous_min = []
        next_min = []
        stack_next = []
        stack_prev = []
        n = len(arr)
        
        for i in range(n):
            previous_min.append(i + 1)
            next_min.append(n - i)
        
            
        for i in range(n):
            
            while stack_prev and stack_prev[-1][0] > arr[i]:
                stack_prev.pop()
            
            previous_min[i] = i - stack_prev[-1][1] if stack_prev else i + 1
            stack_prev.append([arr[i] ,i])
            
            while stack_next and stack_next[-1][0] > arr[i]:
                next_min[stack_next[-1][1]] = i - stack_next[-1][1] 
                stack_next.pop()
            stack_next.append([arr[i],i])
        
        ans = 0
        mod = 10**9 + 7
        
        for i in range(n):
            ans += previous_min[i] * next_min[i] * arr[i]
        
        return ans % mod
        
                
            
        