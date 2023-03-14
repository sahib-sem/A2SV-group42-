# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.ans = []
        self.temp = []
        def inorder(root):
            if not root:
                return 
            if not root.left and not root.right:
                temp = ''.join(self.temp) + str(root.val)
                self.ans.append(temp)
                
            
            
            
            self.temp.append(str(root.val) + '->')
            inorder(root.left)
            inorder(root.right)
            self.temp.pop()
        
        inorder(root)
        
        return self.ans
            
           
            
        
        