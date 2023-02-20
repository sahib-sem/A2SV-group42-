# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=curr2=head
        while curr and curr.next:
            while curr and curr.next and curr.val==curr.next.val:
                curr=curr.next
            curr2.next=curr.next
            curr2=curr2.next
            if curr:
                curr=curr.next
        return head