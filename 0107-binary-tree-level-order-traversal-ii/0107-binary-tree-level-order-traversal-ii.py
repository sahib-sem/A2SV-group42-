# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do level traversal then reverse the list simple as that
        if not root:
            return 
        queue = deque()
        queue.append((root , 0))
        ans = []
        dic = {}
        while queue:
            current_node , idx = queue.popleft()
            if idx not in dic: dic[idx] = []
            dic[idx].append(current_node.val)
            if current_node.left:
                queue.append((current_node.left, idx + 1))
            if current_node.right:
                queue.append((current_node.right , idx + 1))
        
        myKeys = list(dic.keys())
        myKeys.sort(reverse = True)
        dic = {i: dic[i] for i in myKeys}
        for level in dic.values():
            ans.append(level)
        
        return ans
        
            
            
            
            
            
        
        