class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.count = 0
        def backtrack(idx, temp, visited):
            if len(temp) == n:
                self.count += 1
                return 
            
            for i in range(1, idx + 1):
                if i not in visited:
                    curr_idx = len(temp) + 1
                    if i % curr_idx == 0 or curr_idx % i == 0:
                        temp.append(i)
                        visited.add(i)
                        backtrack(idx, temp, visited)
                        temp.pop()
                        visited.remove(i)
        
        backtrack(n, [] , set())
        
        return self.count
                    
            
        