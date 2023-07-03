class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # 100 * 101  = 5050
        
        arr = [0] * 5050
        
        arr[0] = poured
        
        i = 0
        size = 1
        start = 0
        
        
        while i < len(arr):
            should_continue = False
            
            i += 1
            m = i
           
            for j in range(start , start + size): # 0
                rem_cham = arr[j] - 1
                if i >= len(arr):
                    should_continue = False
                    break
                
                if rem_cham > 0:
                    
                    should_continue = True
                    arr[i] += rem_cham / 2
                    arr[i + 1] += rem_cham / 2
                
                i += 1
            
            size += 1
            start = m
            if not should_continue: 
                break
                    
       
        if query_row > 1:
            before_query_row = query_row * (query_row + 1) // 2
        else:
            before_query_row = query_row
            
        index = before_query_row + query_glass
        
        return arr[index] if arr[index] <= 1.0 else 1.0
         
        