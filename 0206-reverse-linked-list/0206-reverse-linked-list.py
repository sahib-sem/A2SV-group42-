# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prevNode,currNode=None,head
        while currNode:
            nextNode=currNode.next
            currNode.next=prevNode
            prevNode=currNode
            currNode=nextNode
        return prevNode
    
            
        
            
                