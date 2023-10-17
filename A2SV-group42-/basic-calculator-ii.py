class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        i  = 0
        while i < len(s):
            
            ele = s[i]
            
            if ele == ' ':
                i += 1
                continue
            
            if ele.isnumeric():
                
                while i < len(s) - 1 and s[i + 1].isnumeric():
                    ele += s[i + 1]
                    i += 1
                
                if stack and (stack[-1] == '*' or stack[-1] == '/'):
                    
                    operator = stack.pop()
                    a = stack.pop()
                    
                    if operator == '*':

                        stack.append(str(int(ele) * int(a)))
                    
                    elif operator == '/':
                        stack.append(str(int(a) // int(ele)))
                        
                else:
                    stack.append(ele)
            
            else:
                
                stack.append(ele)
            
            i += 1
        
        
        
        ans = 0
        positive = True
        for ele in stack:
            
            if ele.isnumeric():
                
                if positive:
                    ans += int(ele)
                else:
                    positive = True
                    ans -= int(ele)
            elif ele == '-':
                positive = False
        
        return ans
            
                
                