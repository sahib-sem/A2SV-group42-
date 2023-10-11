class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        n = len(instructions)
        directions = [(0, 1) , (1, 0), (0, -1), (-1, 0)]
        
        instructions *= 5
        
        current = (0, 0)
        i = 0
        dir_idx = 0
        visited = set({(0, 0, 0, 1, 0)})
        
        while i < len(instructions):
            
            if instructions[i] == 'G':
                
                direction = directions[dir_idx]
                current = (current[0] + direction[0] , current[1] + direction[1], direction[0], direction[1], (i + 1) % n)
                if current in visited:
                    return True
                visited.add(current)

                
            elif instructions[i] == 'L':
                
                dir_idx -= 1
                dir_idx %= 4
                direction = directions[dir_idx]
                current = (current[0] , current[1], direction[0], direction[1], (i + 1) % n)
                if current in visited:
                    return True
                visited.add(current)
            else:
                
                dir_idx += 1
                dir_idx %= 4
            
                direction = directions[dir_idx]
                current = (current[0] , current[1], direction[0], direction[1], (i + 1) % n)
                if current in visited:
                    return True
                visited.add(current)
            
            
            
            
            i += 1
            
            
        return False
                
        
        