class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # nums = int []
        # binary search on the output range
        # [1 , ............. 44]
        #     l   h      
        #      3   6
        def dividedSum(arr , divisor):
            summ = 0
            n = len(arr) 
            
            for i in range(n):
                
                curr = arr[i]
                temp = math.ceil(curr / divisor)
                summ += temp
            return summ 
        
        # difine our bounds 
        low , high =  0 , max(nums) + 1
        
        while low + 1 < high:
            
            mid = low + (high - low) // 2
            
            if dividedSum(nums, mid) > threshold:
                low = mid 
                
            else:
                high = mid 
                
        return high
            
        
            
                
            
            
            
            
        
        
        