# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(root, summ = ''):
            if not root:
                return 
            if not root.left and not root.right:
                summ += str(root.val)
                self.ans += int(summ)
                return
            summ += str(root.val)
            dfs(root.left, summ)
            dfs(root.right, summ)
        
        dfs(root)
        
        return self.ans
        