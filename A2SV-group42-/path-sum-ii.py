# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(curr, ans, lst = [] , total = 0):
            
            if not curr: return 
            
            if not curr.left and not curr.right and total + curr.val == targetSum:
                
                lst.append(curr.val)
                ans.append(lst[:])
                lst.pop()
                return 
            
            
            
            total += curr.val
            lst.append(curr.val)
            dfs(curr.left, ans, lst, total)
            dfs(curr.right, ans, lst, total)
            total -= lst.pop()
        
        ans = []
        dfs(root, ans)
        
        return ans
            
            
            
            
                
            
            
        