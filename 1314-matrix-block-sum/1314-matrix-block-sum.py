class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row , col = len(mat), len(mat[0])
        prefix = [[0 for _ in range(col+1) ] for _ in range(row+1)]
        for r in range(1,row+1):
            for c in range(1,col+1):
                prefix [r][c] = prefix [r][c-1] + prefix [r-1][c] - prefix [r-1][c-1] + mat[r-1][c-1]
        ans = [[0 for _ in range(col) ] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                row1 = i - k if i - k >= 0 else 0
                row2 = i + k  if i + k < row else row - 1
                col1 = j - k if j - k >= 0 else 0
                col2 = j + k if j + k < col else col - 1 
                ans[i][j] = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
        return ans 