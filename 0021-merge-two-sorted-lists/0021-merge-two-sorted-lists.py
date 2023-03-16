# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = self.new_head = ListNode(0)
        
        def merge(h1 , h2):
            if not h1:
                self.new_head.next = h2
                return 
            if not h2:
                self.new_head.next = h1
                return h1
            
            if h1.val < h2.val:
                self.new_head.next = h1
                self.new_head = self.new_head.next
                merge(h1.next , h2)
            else:
                self.new_head.next = h2
                self.new_head = self.new_head.next
                merge(h1, h2.next)
                
        merge(list1, list2)
        
        return dummy.next
        