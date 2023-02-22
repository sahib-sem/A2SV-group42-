# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev,curr=None,slow
        while curr:
            next_node=curr.next
            curr.next=prev
            prev,curr=curr,next_node
        while prev:
            if prev.val!=head.val:
                return False
            prev,head=prev.next,head.next
        return True
        
        
        