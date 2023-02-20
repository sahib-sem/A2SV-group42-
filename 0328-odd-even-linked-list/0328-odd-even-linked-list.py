# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            even=curr1=head.next
        else:
            return head
        curr=head
        while curr and curr.next:
            temp=curr.next.next
            curr.next=temp
            if curr.next:
                curr=curr.next
                curr1.next=curr.next
                curr1=curr1.next
            else:
                break
        curr.next=even
        return head
            
            
            
        