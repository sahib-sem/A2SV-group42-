# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if root and not root.left and not root.right:
            if root.val == targetSum:
                return 1
            else:
                return 0
        self.path = 0
        def recursive(root):
            if not root:
                return []
            if not root.left and not root.right:
                if root.val == targetSum:
                    self.path += 1
                return [root.val]
            
            
            left = recursive(root.left)
            right = recursive(root.right)
            new_lst = [root.val]
            lst = left + right
            if root.val == targetSum:
                self.path += 1
            
            for i in lst:
                val = i + root.val
                if val == targetSum:
                    self.path += 1
                new_lst.append(val)
                
            return new_lst
        
        recursive(root)
        return self.path
            
            
        