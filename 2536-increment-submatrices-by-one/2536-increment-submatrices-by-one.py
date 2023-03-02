class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        row_sum = [[0 for _ in range(n)] for _ in range(n)]
        for query in queries:
            x1 , y1 , x2 , y2 = query
            for i in range(x1 , x2 + 1):
                row_sum[i][y1] += 1
            
                
            if y2 + 1 < n:
                for j in range(x1, x2 + 1):
                    row_sum[j][y2 + 1] -= 1
                    
              
        for i in range(n):
            for j in range(1,n):
                row_sum[i][j] += row_sum[i][j - 1]
                
        return row_sum
                
                
                
        