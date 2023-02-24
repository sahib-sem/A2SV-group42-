class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for operation in logs:
            if operation[:2] == '..':
                if stack:
                    stack.pop()
            if operation[0] != '.':
                stack.append(operation)
        return len(stack)
        