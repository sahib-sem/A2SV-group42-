# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def dfs(curr):
            
            if not curr:
                return [float('-inf'), float('inf') , True]
            
            leftMax, leftMin, leftAns = dfs(curr.left)
            rightMax, rightMin, rightAns = dfs(curr.right)
            
            curr_ans = True
            
            if curr.val <= leftMax:
                curr_ans = False
            
            if curr.val >= rightMin:
                curr_ans = False
            
            
            curr_max = max(leftMax, rightMax, curr.val)
            curr_min = min(leftMin, rightMin, curr.val)
            
            curr_ans = curr_ans and leftAns and rightAns
            
            return [curr_max, curr_min, curr_ans]
        
        return dfs(root)[-1]
            
            
            
            
            
            
            
            
            
                
                
        