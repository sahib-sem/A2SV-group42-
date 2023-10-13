# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left 
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        '''
        n -> n nodes 
        
        left_overs , needed 
        
        
        left = [left_over, needed , count]
        
        
        3 -> 0 -> 0
        
        '''
        
        ans = 0
        def dfs(curr):
            nonlocal ans
            
            if not curr:
                
                return [0, 0]
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            need_curr , left_over_curr = 0, 0
            if curr.val == 0:
                need_curr = 1
                
            if curr.val > 1:
                left_over_curr = curr.val - 1
            
            need = left[1] + right[1] 
            left_over = right[0] + left[0]
            
            ans += need + left_over
            
            need += need_curr
            left_over += left_over_curr
            
            
            if need > left_over:
                
                need -= left_over
                left_over = 0
            else:
                left_over -= need
                need = 0
            
            return [left_over, need]
        
        dfs(root)
        
        return ans
            
            
            
            
            
            
            
            
            
            
            
        