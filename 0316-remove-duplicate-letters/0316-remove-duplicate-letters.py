class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
            
        last_index = {n:i for i,n in enumerate(s)}
        stack = []
        visited = set()
        for idx,char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and last_index[stack[-1]] > idx:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
            
           
        return ''.join(stack)
                
        