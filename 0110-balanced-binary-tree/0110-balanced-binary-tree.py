class Solution:
    def find_height(self,node):
        if not node:
            return [0,0,0]
        if not node.left and not node.right:
            return [1,1,1]
        left = 1
        right = 1
        left += self.find_height(node.left)[-1]
        right += self.find_height(node.right)[-1]

        return [left, right, max(left, right)]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            if not self.isBalanced(root.left):
                return False
                
            l, r, h = self.find_height(root)
            if abs(r - l) <= 1:
                if not self.isBalanced(root.right):
                    return False
                return True
            else:
                return False
                
        return True







    
    
    