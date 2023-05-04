class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0 , 1)])
        visited = set({(0 , 1)})
        level = 0
        while queue:
            
            length = len(queue)
            for _ in range(length):
                
                pos, spd = queue.popleft()
                if pos == target:
                    return level
                
                # A 
                A_speed = spd * 2
                # R
                if spd > 0:
                    R_speed = -1
                else:
                    R_speed = 1
                
                if (spd + pos , A_speed) not in visited:
                    queue.append((spd + pos , A_speed))
                    visited.add((spd + pos, A_speed))
                if (pos, R_speed) not in visited:
                    queue.append((pos, R_speed))
                    visited.add((pos, R_speed))
            
            level += 1
        
                
                
        
        