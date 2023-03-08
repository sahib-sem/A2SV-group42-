# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # traverse level by level and keep track of row, col index 
        lst = [[(0, 0), root]]
        i = 0
        ans = [[0,0,root.val]]
        temp = []
        
        while lst:
            idx , node = lst[i]
            if node.right:
                x , y = idx[0] + 1, idx[1] + 1
                temp.append([(x,y) , node.right])
            if node.left:
                x , y = idx[0] + 1, idx[1] - 1
                temp.append([(x,y) , node.left])
            
            if i >= len(lst) - 1:
                
                
                if temp:
                    
                    for t in temp:
                        idx , node = t
                        ans.append([ idx[1],idx[0], node.val])
                lst = temp
                temp = []
                
                i = 0
            else: 
                i += 1
      
                
        ans.sort()
     
        
        dic = {i[0]:[] for i in ans}
       
        
        for curr in ans:
            dic[curr[0]].append(curr[2])
       
        return [x for x in dic.values()]

        
        
        