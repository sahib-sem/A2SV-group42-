class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        def dfs(node):
            nonlocal visited
            
            visited.add(node)
            
            for nei in rooms[node]:
                if nei not in visited:
                    dfs(nei)
                    
        dfs(0)

        return len(visited) == len(rooms)
        
        
        