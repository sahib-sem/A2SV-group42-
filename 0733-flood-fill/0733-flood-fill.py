class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [[1, 0] , [-1 , 0] , [0, 1] , [0, -1]]
        stack = [(sr, sc)]
        image_copy = []
        for i in range(len(image)):
            temp = []
            for j in range(len(image[0])):
                temp.append(image[i][j])
            image_copy.append(temp)
            
        def inboud(row, col, curr_row, curr_col):
            return 0 <= curr_row <= row - 1 and 0 <= curr_col <= col - 1
        visited = set()
        image_copy[sr][sc] = color
        while stack:
            r, c = stack.pop()
            visited.add((r, c))
            
            for direction in directions:
                change_x , change_y = direction
                new_x, new_y = r + change_x , c + change_y
                if inboud(len(image) , len(image[0]), new_x , new_y) and (new_x , new_y) not in visited:            
                    if image[new_x][new_y] == image[r][c]:
                        image_copy[new_x][new_y] = color
                        image_copy[r][c] = color
                        stack.append((new_x, new_y))
        
        return image_copy
        
                
                