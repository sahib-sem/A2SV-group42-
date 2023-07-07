class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        #traverse backward if you find a element that is greater swap with it 
        
        n = len(arr)
        
        for i in range(n - 2 , - 1, -1):
            
            if arr[i] > arr[i + 1]:
                break
        
        if i == -1:
            return arr
        j = n - 1
        
        while j > 0:
            
            if arr[i] > arr[j] and arr[j] != arr[j - 1]:
                arr[i], arr[j] = arr[j] , arr[i]
                break
            
            j -= 1
        
                
        
        return arr
            
        