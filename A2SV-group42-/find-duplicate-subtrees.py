# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        ans = set({})
        
       
        def dfs(curr, visited = {}):
        
            if not curr:
                return ""
            
            if not curr.left and not curr.right:
                char = str(curr.val)
                if char in visited and not visited[char]:
                    visited[char] = True
                    ans.add(curr)
                if char not in visited:
                    visited[char] = False
                return str(curr.val)
            
            unique_identifier = str(curr.val) + ","
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            unique_identifier = unique_identifier + left + ',' + right
            
            if unique_identifier in visited and not visited[unique_identifier]:
                visited[unique_identifier] = True
                ans.add(curr)
            
            if unique_identifier not in visited:
                visited[unique_identifier] = False
                
            
            return unique_identifier
        
        dfs(root)
        
        return list(ans)
            
            
        
        
            
            
        