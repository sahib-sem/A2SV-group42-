class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['*' , '+' , '/' , '-']
        for token in tokens:
            if token in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                res = str(op2) + str(token) + str(op1)
                res = math.floor(eval(res)) if eval(res) > 0 else math.ceil(eval(res))
                stack.append(res)
                
            else:
                stack.append(token)
        return int(stack[-1])
            
        