# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = root.val
        
        def dfs(node):
            if not node:
                return 0
            
            temp1 = dfs(node.left)
            temp2 = dfs(node.right)
            
            temp1 = max(temp1, 0)
            temp2 = max(temp2, 0)
            
            self.res = max(self.res , node.val + temp1 + temp2)
            
            
            return node.val + max(temp1, temp2)
            
        
        dfs(root)
        
        return self.res
            
        
            
            
        
        
        
        
            
        
        