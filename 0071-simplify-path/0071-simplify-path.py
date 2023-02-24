class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        operations = []
        s = ''
        for char in path:
            if char == '/':
                if s:
                    operations.append(s)
                s = ''
            if char != '/':
                s += char
        if path[-1] != '/':
            operations.append(s)
        for operation in operations:
            if operation == '..':
                if stack:
                    stack.pop()
                continue
            if operation != '.':
                stack.append(operation)

        ans = '/'
        for ele in stack:
            if ele != stack[-1]:
                ans = ans + ele + '/'
            else:
                ans = ans + ele
        return ans
                
        