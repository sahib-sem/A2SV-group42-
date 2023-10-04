class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        # floyd warshal 
        
        isReachable = [[False for _ in range(numCourses)] for __ in range(numCourses)]
        
        for i in range(numCourses):
            isReachable[i][i] = True
        
        for a, b in prerequisites:
            isReachable[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    
                    if isReachable[i][k] and isReachable[k][j]:
                        isReachable[i][j] = True
        
        
        ans = []
        
        for u, v in queries:
            
            ans.append(isReachable[u][v])
        
        return ans
        
        
        
        