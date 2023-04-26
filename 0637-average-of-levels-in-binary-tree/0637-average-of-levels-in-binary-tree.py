# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])
        lst = []
        while queue:
            initial_len = curr_len = len(queue)
            summ = 0 
            while curr_len:
                curr = queue.popleft()
                summ += curr.val
                curr_len -= 1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            
            lst.append(summ / initial_len)
                
        return lst
        