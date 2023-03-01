class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1 , 1]
        arr = [0] * (rowIndex + 1)
        arr[0] = 1
        arr[-1] = 1
        
        before = self.getRow(rowIndex - 1)
        for i in range(1 , rowIndex):
            arr[i] = before[i] + before[i - 1]
            
        return arr
        