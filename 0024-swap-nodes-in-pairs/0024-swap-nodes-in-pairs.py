# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while head:
            if head.next:
                head.val,head.next.val=head.next.val,head.val
            else:
                break
            head=head.next.next
        return dummy
            

            