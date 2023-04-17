# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.ans = 0
        def sum_child(node):
            if not node:
                return 
            if node.left:
                self.ans += node.left.val
            if node.right:
                self.ans += node.right.val
        def dfs(root):
            if root:
                if root.val % 2 == 0:
                    sum_child(root.left)
                    sum_child(root.right)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        
        return self.ans
        