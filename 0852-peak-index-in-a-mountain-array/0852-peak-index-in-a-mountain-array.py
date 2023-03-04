class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # [ 0 , 1 , 2, 3 , 2, 1]
       #l           m            h
         #          l      m      h
        #           l   m    h  
        
        low = -1 
        high = len(arr)
        
        while high > low + 1:
            
            mid = (low + high) // 2
            
            if mid > 0 and mid < len(arr) -1:
                if arr[mid] < arr[mid + 1] and arr[mid] > arr[mid - 1]:
                    low = mid
                else:
                    high = mid
            else:
                low = mid
                
        
        return high
        