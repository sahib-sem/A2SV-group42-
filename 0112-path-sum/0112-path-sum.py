# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(current_node , current_sum):
            if not current_node:
                return False
     
            if not current_node.left and not current_node.right:
                if current_sum + current_node.val == targetSum:
                    return True
                return False
            
            if dfs(current_node.left , current_sum + current_node.val) or dfs(current_node.right, current_sum + current_node.val):
                return True
            
            return False
        
        return dfs(root , 0)
        
        
        
        