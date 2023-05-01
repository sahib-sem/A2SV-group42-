class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        directions = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        
        queue = deque(['0000'])
        visited = set({'0000'})
        step = 0
        while queue:
            
            length = len(queue)
            for _ in range(length):
                current = queue.popleft()
                if current == target:
                    return step
                if current in deadends:
                    continue
                for direction in directions:
                    new_current = ''
                    for i, c in enumerate(current):
                        if int(c) + direction[i] > 9:
                            new_current += '0'
                        elif int(c) + direction[i] < 0:
                            new_current += '9'
                        else:
                            new_current += str(int(c) + direction[i])
                    if new_current not in visited:
                        queue.append(new_current)
                        visited.add(new_current)
            step += 1
        
        return - 1
        