class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        level = 0
        queue = deque([0])
        visited = set()
        
        while queue:
            
            length = len(queue)
            
            for i in range(length):
                
                curr = queue.popleft()
                
                if curr == amount:
                    return level
                
                for coin in coins:
                    if (coin + curr) not in visited and (coin + curr) <= amount:
                        queue.append(coin + curr)
                        visited.add(coin + curr)
                
            level += 1
                    
        
        return -1
                
        