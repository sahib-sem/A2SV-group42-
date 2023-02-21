# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=head
        r=head
        before=None
        for i in range(left-1):
            before=l
            l=l.next
        for j in range(right-1):
            r=r.next
        reverse_head=l
        prev=None
        reverse=False
        while l!=r:
            temp=l.next
            l.next=prev
            prev=l
            l=temp
            reverse=True
        if reverse:
            temp=l.next
            l.next=prev
        if before:
            before.next=l
        else:
            head=l
        if reverse:
            reverse_head.next=temp
        return head

        
            
           