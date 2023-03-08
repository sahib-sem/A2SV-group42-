# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        val1 = p.val
        val2 = q.val
        # LSC is the node where the the two values branch i.e. the node where it is greater than first value and less than the second values or vice versa
        
        current = root
        while current:
            if current.val < val1 and current.val < val2:
                current = current.right
            elif current.val > val1 and current.val > val2:
                current = current.left
            else:
                return current
            
            
            
        