class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row , col = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(col+1) ] for _ in range(row+1)]
        for r in range(1,row+1):
            for c in range(1,col+1):
                prefix[r][c] = prefix[r][c-1] + prefix[r-1][c] -prefix[r-1][c-1] + matrix[r-1][c-1]
        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] -self.prefix[row2+1][col1] + self.prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)