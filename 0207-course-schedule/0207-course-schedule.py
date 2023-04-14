class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # if there is a cycle return false otherwise return true
        
        graph = {node:[] for node in range(numCourses)}
        for a , b in prerequisites:
            graph[a].append(b)
            
        
        for node in range(numCourses):
            
            visited = set() 
            stack = [node]
            visited.add(node)
            target = node

            while stack:

                current = stack.pop()
                for neighbour in graph[current]:
                    
                    if neighbour == target:
                        return False
                    if neighbour not in visited:
                        stack.append(neighbour)
                        visited.add(neighbour)
                
        return True