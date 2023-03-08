# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # two trees are equal if the left and right sub tree are equal
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        
        if p and q:
            if self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right):
                return p.val == q.val
            else: return False
        
            
        
        
            
            
        