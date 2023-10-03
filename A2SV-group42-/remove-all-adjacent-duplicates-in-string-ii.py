class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for char in s:
            
            
            if stack and stack[-1][0] == char:
                if stack[-1][1] + 1 == k:
                    
                    for _ in range(k - 1):
                        stack.pop()
                    
                else:
                    stack.append((char, stack[-1][1] + 1))
            
            else:
                
                stack.append((char, 1))
        
        string = [strr for strr, count in stack ]
        
        return "".join(string)
                
                
                
                
        