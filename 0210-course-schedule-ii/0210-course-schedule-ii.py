class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1
        
        queue = deque() 
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
              
        order = []
        
        while queue:
            
            current = queue.popleft()
            order.append(current)
            
            for nei in graph[current]:
                
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        if len(order) != numCourses:
            return []
        
        return order
                    
            
            
        