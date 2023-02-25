class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        start = 0 
        start2 = 0
        max_length = 0
        max_length2 = 0
            
        for end in range(1,len(arr)):
            if end % 2 == 0 and arr[end] < arr[end - 1]:
                max_length = max(max_length,end - start + 1 )
                
            elif end %2 != 0 and arr[end] > arr[end - 1]:
                max_length = max(max_length,end - start + 1 )
            else: start = end 
                
            if end % 2 == 0 and arr[end] > arr[end - 1]:
                max_length2 = max(max_length2,end - start2 + 1 )
                
            elif end %2 != 0 and arr[end] < arr[end - 1]:
                max_length2 = max(max_length2,end - start2 + 1 )
            else: start2 = end
            
        if max_length == 0 and max_length2 == 0:
            return 1
        else: return max(max_length , max_length2)
        
                
            
            
                
            
        
        