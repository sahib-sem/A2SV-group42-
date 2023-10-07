# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #lca is the first vertex were p and q branch
        
        ans = None

        def dfs(curr):
            nonlocal ans

            if not curr:

                return [False, False]

            res = [False, False]

            if curr.val == p.val:

                res[0] = True
            elif curr.val == q.val:
                res[1] = True

            left = dfs(curr.left)
            right = dfs(curr.right)

            res[0] = res[0] | left[0] | right[0]
            res[1] = res[1] | left[1] | right[1]

            if res[0] and res[1] and not ans:
                ans = curr

            return res 

        dfs(root)

        return ans


                    
                    
            
        