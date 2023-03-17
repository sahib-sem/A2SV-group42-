# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def Valid(root):
            if not root.left and root.right:
                
                right = Valid(root.right)
                res = True
                if not right[2]:
                    res = False
                if root.val >= right[0] or root.val >= right[1]:
                    res = False
                
                return [min(root.val , right[0]) , max(root.val, right[1]) , res]
            if not root.right and root.left:
                
                left = Valid(root.left)
                print(left, root.val)
                res = True
                if not left[2]:
                    res = False
                if root.val <= left[0] or root.val <= left[1]:
                    res = False
                print(res)
                    
                return [min(root.val , left[0]) , max(root.val , left[1]), res]
                    
            if not root.left and not root.right:
                return [root.val, root.val , True]
            
            left_min , left_max , valid1 = Valid(root.left)
            right_min , right_max , valid2 = Valid(root.right)
            if not valid1 or not valid2:
                res = False
            else:
                res = True
                if left_min >= root.val or left_max >= root.val:
                    res = False
                if right_min <=root.val or right_max <= root.val:
                    res = False
            
            return [min(left_min , root.val) , max(right_max , root.val), res]
        
        return Valid(root)[-1]
            
                
                
        
        
            
                
        
        
        
            
        
        