"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.count = 0
        def dfs(node, count):
            if not node:
                return
            if not node.children:
                self.count = max(count, self.count)
                return 
            
            for neighbour in node.children:
                dfs(neighbour , count + 1)
                
        dfs(root, 1)
        
        return self.count