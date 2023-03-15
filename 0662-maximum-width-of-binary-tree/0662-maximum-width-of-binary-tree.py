# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        lst = [(root, 1)]
        max_length = 0
        i = 0
        temp = []
     
        while lst:
            
            node, idx = lst[i]
            
            if node and node.left:
                temp.append((node.left , idx * 2))
        
                
                
            if node and node.right:
                temp.append((node.right, idx * 2 + 1))
                
            
            if i == len(lst) - 1:
                node_ , left = lst[0]
                node_ , right = lst[-1]
                max_length = max(max_length , right - left + 1)
                
                lst = temp
                i = 0
                temp = []
                
                
            else:
                
                i += 1
                
        return max_length
                
                
            
            
        
        
        
        
        
                
        