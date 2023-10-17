# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        
        def dfs(curr):
            nonlocal k
            ans = -1
            if curr:
                
                ans = max(ans, dfs(curr.left))
                k -= 1
                if k == 0:
                    ans = curr.val

                ans = max(dfs(curr.right), ans)
            
            return ans
        return dfs(root)
        