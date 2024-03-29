# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def insertIntoBST(root, val):
            current = parent = root

            if not root:
                return TreeNode(val)

            while current:

                if current.val < val:
                    parent = current 
                    current = current.right

                else:
                    parent = current 
                    current = current.left

            if parent.val > val:
                parent.left = TreeNode(val)

            else:
                parent.right = TreeNode(val)

            return root
        root = None
        for i in preorder:
            root = insertIntoBST(root, i)
            
        return root