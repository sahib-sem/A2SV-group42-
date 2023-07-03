# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(curr_node, rob):
            if not curr_node:
                return 0
            
            if not curr_node.left and not curr_node.right:
                if rob:
                    return curr_node.val
                else:
                    return 0
            state = (curr_node, rob)
            
            if state not in memo:
                if rob:
                    ans1 = curr_node.val + dp(curr_node.left , not rob) + dp(curr_node.right , not rob)
                    ans2 = dp(curr_node.left , rob) + dp(curr_node.right , rob)
                    ans1 = max(ans1, ans2)
                else:
                    ans1 = dp(curr_node.left, not rob) + dp(curr_node.right , not rob)
                
                memo[state] = ans1
            return memo[state]
        
        return max(dp(root, True) , dp(root, False))
                
            