# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        # prefix = {10: 1, 15:1, 18:1}
        
        self.ans = 0
        
        def dfs(curr, prefix = {0:1}, running_sum = 0):
            
            if not curr:
                return 
        
            
            
            running_sum += curr.val
            self.ans += prefix.get(running_sum - targetSum , 0)
            prefix[running_sum] = prefix.get(running_sum, 0) + 1
            
            dfs(curr.left, prefix, running_sum)
            dfs(curr.right, prefix, running_sum)
            
            prefix[running_sum] -= 1
            
            if prefix[running_sum] == 0:
                del prefix[running_sum]
            
        dfs(root)
        
        return self.ans
            
            
        