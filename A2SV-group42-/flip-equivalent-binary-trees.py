# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def valid(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return node1.val == node2.val
        
        def dfs(curr1, curr2):
            
            if not curr1 and not curr2:
                return True
            
            if not curr1 or not curr2:
                return False
            
            currLeft1 , currRight1 = curr1.left , curr1.right
            currLeft2 , currRight2 = curr2.left , curr2.right
            
            ans = False
            
            if valid(currLeft1, currLeft2) and valid(currRight1, currRight2):
                ans = dfs(curr1.left, curr2.left) and dfs(curr1.right, curr2.right) or             dfs(curr1.right, curr2.right) and dfs(curr1.left, curr2.left)
            
            if valid(currLeft1, currRight2) and valid(currLeft2, currRight1):
                ans = dfs(curr1.left, curr2.right ) and dfs(curr1.right, curr2.left)
            
            return ans
        
        if root1 and root2 and (root1.val != root2.val):
            return False
        return dfs(root1, root2)
            
            
            
            
            
            
            
            
            
            
            
            
            
        