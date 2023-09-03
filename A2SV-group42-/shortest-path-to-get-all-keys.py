class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        # level travesal from @
        key_letter = ['a', 'b', 'c' , 'd' , 'e' , 'f']
        lock_letter = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']
        count = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '@':
                    start = (r, c)
                if grid[r][c].isalpha():
                    count.add(grid[r][c].lower())
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        def isValid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'
        
        
        queue = deque([(start, set() , 0, set({(start[0], start[1], ())}))]) # start_position , collected_keys, steps, visited
        Num_keys = len(count)

        
        while queue:

            (x, y) ,collected_keys, steps , visited  = queue.popleft()
            
        
            
            if grid[x][y] in key_letter:
                collected_keys.add(grid[x][y])
                if len(collected_keys) == Num_keys:
                    return steps
                

            for ch_x, ch_y in directions:

                new_x, new_y = x + ch_x, y + ch_y
                ck_in_set = tuple(sorted(list(collected_keys)))
                if isValid(new_x, new_y) and (new_x, new_y, ck_in_set) not in visited:
                    if grid[new_x][new_y] in lock_letter and grid[new_x][new_y].lower() not in collected_keys:
                        continue
                    visited.add((new_x, new_y, ck_in_set))
                    queue.append(((new_x, new_y), collected_keys.copy(), steps + 1, visited))
                    

            
        
        return -1
                           
                
        
        