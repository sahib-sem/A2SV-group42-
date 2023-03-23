# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def balanced(root):
            if  root == None:
                return [True, 0]
            if not root.left and not root.right:
                return [True , 1]
            
            left = balanced(root.left)
            right = balanced(root.right)
            
            if left[0] and right[0]:
                if abs(right[1] - left[1]) > 1:
                    return [False , 0]
                    
                return [True, max(left[1], right[1]) + 1]
            return [False,0]
        
        
        
        return balanced(root)[0]
    
    
    