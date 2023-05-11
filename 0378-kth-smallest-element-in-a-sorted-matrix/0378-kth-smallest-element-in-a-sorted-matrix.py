class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0] , i, 0) )
            
        while heap and k > 0:
            k -= 1 
            num, arr_idx , ele_idx = heapq.heappop(heap)
            ans = num
            
            if ele_idx < len(matrix[arr_idx]) - 1:
                heapq.heappush(heap, (matrix[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))
        
        return ans 
                
            
            
        
        
        