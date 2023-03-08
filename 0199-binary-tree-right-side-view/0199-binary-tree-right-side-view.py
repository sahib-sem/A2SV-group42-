# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = [root.val]
        
        # same as the level travesal just add the last element 
        temp = []
        lst = [root]
        i = 0
        
        while lst:
            node = lst[i]
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if i >= len(lst) - 1:
                if temp:
                    output.append(temp[-1].val)
                lst = temp
                temp = []
                i = 0
            else:
                i += 1
                
        return output
        
                
        