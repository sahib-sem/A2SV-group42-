# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # leave nodes are always equal to the average of its subtrees(which is none) 
        #base cases when we reach leave node or none
        self.ans = 0 # global variable to keep the count 
        
        def numOfAverage(root):
            if not root:
                return [0,0]
            
            if not root.left and not root.right:
                self.ans += 1
                return [root.val , 1]
            
            left_sum = numOfAverage(root.left)
            right_sum = numOfAverage(root.right)
            
            summ = left_sum[0] + right_sum[0] + root.val
            denominator = left_sum[1] + right_sum[1] + 1
            
            if summ // denominator == root.val:
                self.ans += 1
                
            return [summ , denominator]
        
        numOfAverage(root)
        
        return self.ans
    
                
            
            