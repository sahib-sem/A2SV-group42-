# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build undirected graph
        
        graph = defaultdict(list)
        
        stack = [root]
        while stack:
            
            current = stack.pop()
            left, right = current.left, current.right
            if left:
                graph[current.val].append(left.val)
                graph[left.val].append(current.val)
                stack.append(left)
            if right:
                graph[current.val].append(right.val)
                graph[right.val].append(current.val)
                stack.append(right)
        # from the target perform bfs
        queue = collections.deque()
        queue.append(target.val)
        visited = set({target.val})
        level = 0
        
        while queue:
            
            length = len(queue)
            if k == level:
                print(list(queue))
                return list(queue)
            for _ in range(length):
                current = queue.popleft()
                
                for nei in graph[current]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            level += 1
        
        return list(queue)
            
                
        