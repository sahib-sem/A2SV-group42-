# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = {}
        
        def inorder(root):
            
            if root:
                inorder(root.left)
                count[root.val] = count.get(root.val, 0) + 1
                inorder(root.right)
                
        inorder(root)
        maxx = max(count.values())
        
        ans = []
        for key , val in count.items():
            if val == maxx:
                ans.append(key)
        return ans
        
            
        
        
                
            
            
            
        