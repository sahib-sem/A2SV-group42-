class Solution:
    def spiralOrder(self, inputMatrix: List[List[int]]) -> List[int]:
        
        def inbound(x, y):
            return 0 <= x < len(inputMatrix) and 0 <= y < len(inputMatrix[0])
        directions =  [
               (-1, 0), 
               (0, 1), 
               (1, 0), 
               (0, -1)
               ]
        ans = []
  # [[1]]  
        def dfs(r, c, parent_x, parent_y, visited):
    
            visited.add((r, c))
            ans.append(inputMatrix[r][c])

            new_x, new_y = r + parent_x, c + parent_y
    
            if inbound(new_x, new_y) and (new_x, new_y) not in visited:
                dfs(new_x, new_y, parent_x, parent_y, visited)
                return 
    
            for change_x , change_y in directions:
                new_x, new_y = r + change_x , c + change_y
                if inbound(new_x, new_y) and (new_x, new_y) not in visited:
        
                    dfs(new_x, new_y, change_x, change_y, visited)
        
        dfs(0, 0,  -1, -1, set())
        
        return ans
